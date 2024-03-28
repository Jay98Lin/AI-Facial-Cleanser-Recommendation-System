# LINE Bot:
本項目為開發LINE Bot介面的主程式，旨在幫助用戶根據洗面乳的實際使用效果選擇合適的產品。系統通過分析用戶上傳的洗面乳圖片，返回相應的產品評價、評分及推薦。


## 洗面乳辨識與評價LINE Bot

```plaintext
│
├── config.ini
│   └── 包含MySQL數據庫配置和LINE Messaging API的設定。
│
├── 1_linebot_main.py
│   └── 主要的Flask應用程式文件，處理LINE Messaging API的Webhook請求。
│
├── Dockerfile
│   └── 定義了如何在Docker容器中構建Flask應用程式的環境。
│
├── requirements.txt
│   └── 列出了項目所需的所有Python依賴包。
│
├── select_tool_v2.py
│   └── 包含數據庫查詢和處理邏輯的工具函式，例如從數據庫中選擇產品詳情和生成回應訊息的JSON模板。
│
└── JSON模板
    ├── v1.json
    │   └── 定義了用於展示單個產品詳情的LINE Flex Message模板。
    │
    ├── v2.json
    │   └── 定義了用於展示推薦產品的LINE Carousel Flex Message模板。
    │
    └── v3.json
        └── 用於特定互動或功能的另一種Flex Message模板。
```

## 配置config.ini文件：

```plaintext
[line-bot]
channel_access_token=YOUR_CHANNEL_ACCESS_TOKEN
channel_secret=YOUR_CHANNEL_SECRET
```

```plaintext
[mysql]
host=YOUR_MYSQL_HOST
user=YOUR_MYSQL_USER
password=YOUR_MYSQL_PASSWORD
database=YOUR_DATABASE_NAME
```

## 運行項目：

```plaintext
python 1_linebot_main.py
```

## 貢獻
歡迎通過GitHub Issue或Pull Request方式貢獻代碼或提出改進建議。
