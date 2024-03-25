#洗面乳識別系統
本項目是一個基於LINE Bot的洗面乳圖像識別系統，使用了Keras的MobileNetV2進行遷移式訓練，並結合了爬蟲和自然語言處理（NLP）技術來分析和獲取網絡上的相關產品評價。整個服務部署在Google Cloud Run上。

##特點
圖像識別：利用Keras的MobileNetV2模型進行遷移式學習，訓練了專門針對洗面乳產品的圖像識別系統。
自動爬蟲：自動抓取網絡上的洗面乳產品評價。
NLP文本分析：分析抓取到的評價文本，提供用戶更多維度的產品信息。
LINE Bot交互：用戶可以通過LINE Bot上傳洗面乳圖片，系統將返回識別結果及相關評價。

##技術棧
Python
Keras & TensorFlow
自然語言處理（NLP）
LINE Messaging API
Google Cloud Run
爬蟲技術
快速開始
說明如何本地運行項目和部署到Google Cloud Run。

前提條件
列出運行和部署項目所需的環境和工具，例如Python版本，必要的API密鑰等。

安裝和運行
提供一步步的指南，說明如何安裝必要的依賴、如何本地運行項目以及如何部署到Google Cloud Run。

bash
Copy code
# 克隆倉庫
git clone https://github.com/Jay98Lin/AI-Project.git

# 安裝依賴
pip install -r requirements.txt

# 本地運行
python app.py

# 部署到Google Cloud Run
# 提供具體的部署命令或步驟
使用說明
說明用戶如何與LINE Bot互動，包括如何發送圖片，以及如何理解系統返回的信息。

