# 使用官方的 Python 執行環境作為基本的 Docker 影像
FROM python:alpine3.7

# 維護者： docker_user <docker_user at email.com> (@docker_user)
MAINTAINER yenming yenming@raylios.com

# 建立檔案工作區
RUN mkdir -p /usr/src/app  && \
    mkdir -p /var/log/gunicorn

# 設定工作目錄為 /usr/src/app
WORKDIR /usr/src/app

# 複製目前目錄下的內容, 放進 Docker 容器中的 /usr/src/app
COPY . /usr/src/app

# 安裝 requirements.txt 中所列的必要套件, 並延長安裝時間
RUN pip install --default-timeout=100 --no-cache-dir gunicorn && \
    pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# 讓 80 連接埠可以從 Docker 容器外部存取
ENV PORT 80
EXPOSE 80

# 當 Docker 容器啟動時, 自動執行 ai-web-raylios.py
# Gunicorn 是一個 Python WSGI Unix - http web service, 開啟2個 worker
CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", ":80", "ai-web-raylios:app"]

