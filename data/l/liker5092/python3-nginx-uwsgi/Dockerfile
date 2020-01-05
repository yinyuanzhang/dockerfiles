FROM ubuntu:18.04

# 更换源并安装系统软件

RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
         gcc \
         vim \
         wget \
         python3 \
         python3-all-dev \
         nginx \
         sqlite3 \
    && apt-get upgrade -y \
    && wget -c -O get-pip.py --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && pip3 -V \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf get-pip.py \
    && rm -rf /var/lib/apt/lists/*
	
# 工作站点，需要将你的项目和本文件放到一个目录下再创建
WORKDIR /site
COPY . .

# 运行测试点
RUN pip3 install -r /site/requirements.txt \
    && mkdir /test \
    && django-admin startproject project /test/


# 默认的端口
EXPOSE 8000

# 默认运行测试下的项目。
CMD ["python3","/test/manage.py","runserver","0.0.0.0:8000"]


# 你自己的站点的运行命令
# docker run --name yourname -it --rm -v "$PWD":/site -w /site --privileged=true -p 0.0.0.0:8000:8000 liker5092/python3-nginx-uwsgi bash -c "pip3 install -r requirements.txt && python3 manage.py runserver 0.0.0.0:8000"

# 示例测试的站点
# docker run --rm python3-nginx-uwsgi:v1
