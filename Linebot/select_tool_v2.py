import pymysql, json, configparser


config = configparser.ConfigParser()
config.read('config.ini')

host = config.get('mysql', 'host')
port = int(config.get('mysql', 'port'))
user = config.get('mysql', 'user')
passwd = config.get('mysql', 'passwd')
db = config.get('mysql', 'db')
charset = config.get('mysql', 'charset')
end_point = config.get('line-bot', 'end_point')


mark = {
        0: "FOAM", 1: "上山採藥", 2: "肌研", 3: "肌研", 4: "肌研",
        5: "莎娜", 6: "露姬婷", 7: "清妍", 8: "專科", 9: "高絲",
        10: "Biore", 11: "Biore", 12: "Bifesta", 13: "Biore", 14: "露姬婷",
        15: "Bifesta", 16: "Bifesta", 17: "Bifesta"
}

urls = {
    0: 'https://www.cosme.net.tw/products/87330/reviews',
    1: 'https://www.cosme.net.tw/products/4989/reviews',
    2: 'https://www.cosme.net.tw/products/85513/reviews',
    3: 'https://www.cosme.net.tw/products/79415/reviews',
    4: 'https://www.cosme.net.tw/products/40527/reviews',
    5: 'https://www.cosme.net.tw/products/19398/reviews',
    6: 'https://www.cosme.net.tw/products/79637/reviews',
    7: 'https://www.cosme.net.tw/products/90191/reviews',
    8: 'https://www.cosme.net.tw/products/105363/reviews',
    9: 'https://www.cosme.net.tw/products/57958/reviews',
    10: 'https://www.cosme.net.tw/products/67787/reviews',
    11: 'https://www.cosme.net.tw/products/58118/reviews',
    12: 'https://www.cosme.net.tw/products/89784/reviews',
    13: 'https://www.cosme.net.tw/products/67788/reviews',
    14: 'https://www.cosme.net.tw/products/36729/reviews',
    15: 'https://www.cosme.net.tw/products/82073/reviews',
    16: 'https://www.cosme.net.tw/products/82072/reviews',
    17: 'https://www.cosme.net.tw/products/82074/reviews'
}

imgs = {
    0: "https://storage.googleapis.com/aiface/Q/0.jpg",
    1: "https://storage.googleapis.com/aiface/Q/1.jpg",
    2: "https://storage.googleapis.com/aiface/Q/2.jpg",
    3: "https://storage.googleapis.com/aiface/Q/3.jpg",
    4: "https://storage.googleapis.com/aiface/Q/4.jpg",
    5: "https://storage.googleapis.com/aiface/Q/5.jpg",
    6: "https://storage.googleapis.com/aiface/Q/6.jpg",
    7: "https://storage.googleapis.com/aiface/Q/7.jpg",
    8: "https://storage.googleapis.com/aiface/Q/8.jpg",
    9: "https://storage.googleapis.com/aiface/Q/9.jpg",
    10: "https://storage.googleapis.com/aiface/Q/10.jpg",
    11: "https://storage.googleapis.com/aiface/Q/11.jpg",
    12: "https://storage.googleapis.com/aiface/Q/12.jpg",
    13: "https://storage.googleapis.com/aiface/Q/13.jpg",
    14: "https://storage.googleapis.com/aiface/Q/14.jpg",
    15: "https://storage.googleapis.com/aiface/Q/15.jpg",
    16: "https://storage.googleapis.com/aiface/Q/16.jpg",
    17: "https://storage.googleapis.com/aiface/Q/17.jpg"
}


def select_1(product_id):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    print('Successfully connected!')
    cursor = conn.cursor()

    sql = f"""
    select ID, 簡稱, 平均分數, 效果, 優點, 缺點, 推薦1, 推薦2, 推薦3 from items_table
    where ID = {product_id};
    """
    cursor.execute(sql)
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def select_2(product_id, age_type):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    print('Successfully connected!')
    cursor = conn.cursor()

    sql = f"""
    select {age_type}分數, {age_type}效果 from items_table
    where ID = {product_id};
    """
    cursor.execute(sql)
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def stars_1(js, math):
    star = {
    "type": "icon",
    "size": "lg",
    "url": "https://imgur.com/ZCwfMp0.png"
    }

    starhelf = {
        "type": "icon",
        "size": "lg",
        "url": "https://imgur.com/eIiB8Qn.png"
    }

    starlast = {
        "type": "text",
        "text": f"{math}",
        "size": "sm",
        "margin": "md",
        "color": "#111111",
        "offsetTop": "none",
        "offsetBottom": "none",
        "offsetStart": "none",
        "offsetEnd": "none"
    }

    for i in range(int(math)):
        js["body"]["contents"][2]["contents"].append(star)

    num = int(math * 10 % 10)
    if num >= 7 and num <= 9:
        js["body"]["contents"][2]["contents"].append(star)
        js["body"]["contents"][2]["contents"].append(starlast)
    elif num >= 4 and num <= 6:
        js["body"]["contents"][2]["contents"].append(starhelf)
        js["body"]["contents"][2]["contents"].append(starlast)
    else:
        js["body"]["contents"][2]["contents"].append(starlast)

    return js


def stars_2(js, math, info_number):
    star = {
    "type": "icon",
    "size": "lg",
    "url": "https://imgur.com/ZCwfMp0.png"
    }

    starhelf = {
        "type": "icon",
        "size": "lg",
        "url": "https://imgur.com/eIiB8Qn.png"
    }

    starlast = {
        "type": "text",
        "text": f"{math}",
        "size": "sm",
        "margin": "md",
        "color": "#111111",
        "offsetTop": "none",
        "offsetBottom": "none",
        "offsetStart": "none",
        "offsetEnd": "none"
    }

    for i in range(int(math)):
        js['contents'][info_number]["body"]["contents"][2]["contents"].append(star)

    num = int(math * 10 % 10)
    if num >= 7 and num <= 9:
        js['contents'][info_number]["body"]["contents"][2]["contents"].append(star)
        js['contents'][info_number]["body"]["contents"][2]["contents"].append(starlast)
    elif num >= 4 and num <= 6:
        js['contents'][info_number]["body"]["contents"][2]["contents"].append(starhelf)
        js['contents'][info_number]["body"]["contents"][2]["contents"].append(starlast)
    else:
        js['contents'][info_number]["body"]["contents"][2]["contents"].append(starlast)

    return js


def load_js1(data):
    with open('v1.json', mode='r', encoding='utf-8') as fi:
        js = json.load(fi)

    math = data[2]
    js = stars_1(js, math)

    js["body"]["contents"][0]["text"] = mark[data[0]]  # 品牌
    js['body']['contents'][1]['text'] = data[1]  # 商品名稱
    js['body']['contents'][3]['contents'][0]['contents'][1]['text'] = data[3]  # 效果
    js['body']['contents'][3]['contents'][1]['contents'][1]['text'] = data[4] # 優點
    js["body"]["contents"][3]["contents"][1]["contents"][2]["contents"][1]["text"] = data[5] # 缺點
    js['footer']['contents'][1]['action']['text'] = f"推薦:{data[1]}"  # 推薦商品
    js['hero']['url'] = imgs[data[0]]  # 圖片
    js['footer']['contents'][0]['action']['uri'] = urls[data[0]]  # 網址
    
    return js


def load_js2(data):
    with open('v2.json', mode='r', encoding='utf-8') as fi:
        js = json.load(fi)

    for info_number in range(3):
        math = data[info_number][2]
        js = stars_2(js, math, info_number)

        js['contents'][info_number]["body"]["contents"][0]["text"] = mark[data[info_number][0]]  # 品牌
        js['contents'][info_number]['body']['contents'][1]['text'] = data[info_number][1]  # 商品名稱
        js['contents'][info_number]['body']['contents'][3]['contents'][0]['contents'][1]['text'] = data[info_number][3]  # 效果
        js['contents'][info_number]['body']['contents'][3]['contents'][1]['contents'][1]['text'] = data[info_number][4] # 優點
        js['contents'][info_number]["body"]["contents"][3]["contents"][1]["contents"][2]["contents"][1]["text"] = data[info_number][5] # 缺點
        js['contents'][info_number]['footer']['contents'][1]['action']['text'] = f"推薦:{data[info_number][1]}"  # 推薦商品
        js['contents'][info_number]['hero']['url'] = imgs[data[info_number][0]]  # 圖片
        js['contents'][info_number]['footer']['contents'][0]['action']['uri'] = urls[data[info_number][0]]  # 網址
    
    return js


def push_db(id_tp):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    print('Successfully connected!')
    cursor = conn.cursor()

    sql = f"""
    select ID, 簡稱, 平均分數, 效果, 優點, 缺點, 推薦1, 推薦2, 推薦3 from items_table
    where ID = {id_tp[0]} or ID = {id_tp[1]} or ID = {id_tp[2]};
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    info = []
    for i in id_tp:
        for x in range(3):
            if data[x][0] == i:
                info.append((data[x]))  # 調整排序問題

    cursor.close()
    conn.close()

    return info
