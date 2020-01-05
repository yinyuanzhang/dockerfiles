FROM ubuntu:16.04

# System and Python 3
RUN set -ex; \
    apt-get update && apt-get install -qqy \
    nginx \
    git \
    python3 \
    python3-dev \
    python3-pip \
    python3-mysql.connector \
    software-properties-common

# Video Processing itself
RUN set -ex; apt-get update && apt-get install -qqy ffmpeg

# Certbot
RUN set -ex; add-apt-repository ppa:certbot/certbot
RUN set -ex; apt update
RUN set -ex; apt-get install -y python-certbot-nginx

RUN set -ex; pip3 install flask
RUN set -ex; pip3 install Jinja2
RUN set -ex; pip3 install WTForms
RUN set -ex; pip3 install multidict
RUN set -ex; pip3 install pytz
RUN set -ex; pip3 install gunicorn
RUN set -ex; pip3 install flask_limiter
RUN set -ex; pip3 install requests
RUN set -ex; pip3 install flask-restplus
RUN set -ex; pip3 install Flask-Caching
RUN set -ex; pip3 install SQLAlchemy
RUN set -ex; pip3 install Flask-SQLAlchemy
RUN set -ex; pip3 install APScheduler
RUN set -ex; pip3 install flask-cors
RUN set -ex; pip3 install Flask-Header-Session==0.0.4
RUN set -ex; pip3 install sqlacodegen
RUN set -ex; pip3 install jsonschema
RUN set -ex; pip3 install pycrypto
RUN set -ex; pip3 install redis


# Aliyun
RUN set -ex; pip3 install aliyun-python-sdk-jaq
RUN set -ex; pip3 install aliyun-python-sdk-sts
RUN set -ex; pip3 install oss2

# YunPian
RUN set -ex; pip3 install yunpian-python-sdk

# Log formatter of json
RUN set -ex; pip3 install python-json-logger

# Image Processing
RUN set -ex; pip3 install Pillow
# Video Processing binding
RUN set -ex; pip3 install ffmpeg-python

# Database Migration
RUN set -ex; pip3 install flask_migrate

# Flask Auth
RUN set -ex; pip3 install flask_httpauth

# Py JWT
RUN set -ex; pip3 install pyjwt

RUN set -ex; pip3 install elasticsearch
RUN set -ex; pip3 install elasticsearch-dsl

# Celery
RUN set -ex; pip3 install celery

# Face Recog
RUN set -ex; apt install -qqy cmake
RUN set -ex; pip3 install face_recognition

# Other dependencies
ADD requirements.txt ./
RUN set -ex; pip3 install -r requirements.txt
