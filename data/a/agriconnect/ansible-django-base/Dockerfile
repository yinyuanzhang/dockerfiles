FROM alpine:latest

MAINTAINER Nguyễn Hồng Quân <ng.hong.quan@gmail.com>


ENV LANG en_US.UTF-8
# Ref: https://github.com/William-Yeh/docker-ansible/
RUN apk --update add bash python3 build-base rsync && \
    apk add sshpass openssh-client openssl ca-certificates git && \
    apk add postgresql-dev libffi-dev python3-dev jpeg-dev yaml-dev zlib-dev linux-headers && \
    pip3 install -U pip wheel && pip3 install cffi --extra-index-url https://pypi.agriconnect.vn/musl/simple/ && \
    pip3 install cryptography --extra-index-url https://pypi.agriconnect.vn/musl/simple/ && \
    pip3 install ansible && \
    pip3 install Pillow psycopg2 pytest-flakes pytest-django && \
    mkdir -p /etc/ansible && echo 'localhost' > /etc/ansible/hosts && \
    rm -rf /var/cache/apk/* && rm -rf /root/.cache/pip && \
    sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd
