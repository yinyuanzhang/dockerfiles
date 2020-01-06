FROM tangchen2018/python:3.6-alpine
ENV PYTHONUNBUFFERED 1

COPY . /project/sso

WORKDIR /project/sso

RUN pip install -r requirements.txt \
    && mkdir -p /project/sso/logs \
    && mkdir -p /project/sso/media

RUN apk add --no-cache tzdata  && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

CMD ["uwsgi", "/project/sso/sso/wsgi/uwsgi.ini"]
