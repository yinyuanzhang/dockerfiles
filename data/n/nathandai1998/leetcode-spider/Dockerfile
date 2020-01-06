FROM python:3.6.8-slim-stretch
LABEL MAINTAINER NathanDai daizheng1998@qq.com

WORKDIR /app
COPY requirements.txt /app
ENV TZ Asia/Shanghai
RUN pip install -r requirements.txt

COPY . /app

CMD ["python","main.py"]