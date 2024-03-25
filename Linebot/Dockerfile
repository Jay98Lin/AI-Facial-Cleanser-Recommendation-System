FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 设置时区
ENV TZ=Asia/Taipei

# 安装系统依赖，包括 libglib2.0-0 和其他可能需要的依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 复制 Python 依赖文件
COPY requirements.txt ./

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

CMD ["python", "main_v5.py"]