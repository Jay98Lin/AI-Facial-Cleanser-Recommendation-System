import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import matplotlib as mpl
from tensorflow.keras import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

# 設定輸入資料夾的路徑
input_folder = "test_photo"
# 設定輸出資料夾的路徑
output_folder = "test_photo/result"

# 載入預訓練模型
model_ai = keras.applications.MobileNetV2(weights="imagenet", include_top=True)

# 如果輸出資料夾不存在，則建立它
os.mkdir(output_folder)

# 獲取輸入資料夾中所有檔案的清單
files = os.listdir(input_folder)

# 定義最後一個卷積層
last_conv_layer_name = "out_relu"
last_conv_layer_model = Model(
    inputs=model_ai.input, outputs=model_ai.get_layer(last_conv_layer_name).output
)

# 逐一處理輸入資料夾中的所有檔案
for file in files:
    # 建立輸入影像的完整路徑
    input_path = os.path.join(input_folder, file)

    # 初始化 superimposed_img 為 None
    superimposed_img = None

    try:
        # 載入並預處理影像
        img = image.load_img(input_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # 獲取最後一個卷積層的輸出
        last_conv_layer_output = last_conv_layer_model(img_array)

        # 用正確的分類器層名稱替換 'dense' 和 'dense_1'
        classifier_layer_names = [
            "global_average_pooling2d",
            "predictions",  # 使用 'predictions' 而不是 'dense'
        ]

        # 調整分類器模型的輸入形狀
        classifier_input = keras.Input(shape=last_conv_layer_output.shape[1:])
        x = classifier_input

        for layer_name in classifier_layer_names:
            x = model_ai.get_layer(layer_name)(x)

        classifier_model = keras.Model(classifier_input, x)

        # 使用 GradientTape 計算梯度
        with tf.GradientTape() as tape:
            last_conv_layer_output = last_conv_layer_model(img_array)
            tape.watch(last_conv_layer_output)
            preds = classifier_model(last_conv_layer_output)
            top_pred_index = tf.argmax(preds[0])
            top_class_channel = preds[:, top_pred_index]
            grads = tape.gradient(top_class_channel, last_conv_layer_output)

        # 梯度池化及 channel 重要性加權
        # 會計算出一個向量，它的每個元素都是特定 channel 的平均梯度(它量化了每個 channel 對最高分類別的重要程度)
        # 會陸續沿著第 0,1,2 軸做平均，因此這三軸會消失，最後只剩下第 3 軸(channel)
        pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2)).numpy()
        last_conv_layer_output = last_conv_layer_output.numpy()[0]
        for i in range(pooled_grads.shape[-1]):

            # 每一個通道的特徵圖乘上對應的權重
            last_conv_layer_output[:, :, i] *= pooled_grads[i]
            
        # 得到特徵圖的逐通道平均值，即為類激活的熱力圖
        heatmap = np.mean(last_conv_layer_output, axis=-1)

        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)

        # 載入原始影像
        img = keras.preprocessing.image.load_img(input_path)
        img = keras.preprocessing.image.img_to_array(img)

        # 將熱力圖中的數值調整到 0-255 之間
        heatmap = np.uint8(255 * heatmap)

        # 使用 jet 色盤對熱力圖著色(以下三行)
        jet = mpl.cm.get_cmap("jet")

        jet_colors = jet(np.arange(256))[:, :3]
        jet_heatmap = jet_colors[heatmap]

        # 創建一個包含重新著色之熱力圖的影像(以下三行)
        jet_heatmap = keras.preprocessing.image.array_to_img(jet_heatmap)
        jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
        jet_heatmap = keras.preprocessing.image.img_to_array(jet_heatmap)

        # 疊加熱力圖與原圖，熱力圖的不透明度為 80%
        superimposed_img = jet_heatmap * 0.8 + img
        superimposed_img = keras.preprocessing.image.array_to_img(superimposed_img)

    except PermissionError as e:
        print(f"PermissionError: {e}")
        continue  # 跳到下一次迴圈

    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     continue  # 跳到下一次迴圈

    # 儲存疊加後的影像
    output_path = os.path.join(output_folder, f"result_{file}")
    superimposed_img.save(output_path)
