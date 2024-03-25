# 洗面乳識別系統
本項目是一個基於LINE Bot開發的洗面乳圖像識別系統，使用了Keras的MobileNetV2進行遷移式訓練，並結合了爬蟲和自然語言處理（NLP）技術來分析和獲取網絡上的相關產品評價。整個服務部署在Google Cloud Run上。

## 特點
**1. 圖像識別**：利用Keras的MobileNetV2模型進行遷移式學習，訓練了專門針對洗面乳產品的圖像識別系統。  
**2. 自動爬蟲**：自動抓取網絡上的洗面乳產品評價。  
**3. NLP文本分析**：分析抓取到的評價文本，提供用戶更多維度的產品信息。  
**4. LINE Bot互動**：用戶可以通過LINE Bot上傳洗面乳圖片，系統將返回識別結果及相關評價。  

## 技術線
- Python  
- Keras & TensorFlow   
- 網路爬蟲  
- 自然語言處理（NLP）  
- LINE Messaging API  
- Google Cloud Run  

## 前提條件
- Python版本: 3.8
- Tensorflow版本: 2.4.0
- LINE Developers設定:
  - `channel_access_token`: [你的channel_access_token]
  - `channel_secret`: [你的channel_secret]
  - `end_point`: [你的end_point]
- MySQL設定:
  - `host`: [你的MySQL主機地址]
  - `port`: 3306
  - `user`: [你的MySQL用戶名]
  - `passwd`: [你的MySQL密碼]
- GCP帳戶



## 安裝和運行
提供一步步的指南，說明如何安裝必要的依賴、如何本地運行項目以及如何部署到Google Cloud Run。

bash
Copy code

1. 下載完整檔案：git clone https://github.com/Jay98Lin/AI-Project.git  

## 安裝依賴
pip install -r requirements.txt

## 本地運行
Linebot資料夾中的主程式：1_linebot_main.py

部署到Google Cloud Run

## 使用說明
說明用戶如何與LINE Bot互動，包括如何發送圖片，以及如何理解系統返回的信息。

## 貢獻指南
鼓勵更多的開發者參與進來，對於如何貢獻代碼、報告問題或提供功能建議給出說明。

## 致謝
感謝所有使用和支持本項目的人。
特別感謝所有對項目代碼做出貢獻的開發者。

