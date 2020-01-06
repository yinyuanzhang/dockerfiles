FROM python:3.7-rc-alpine3.7
RUN echo "https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories \
    &&  apk update && apk upgrade \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev openssh netcat-openbsd tzdata bash rsync && cp -r -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

USER root
COPY provision.sh /tmp/provision.sh
RUN chmod +x /tmp/provision.sh && sh /tmp/provision.sh
USER $original_user