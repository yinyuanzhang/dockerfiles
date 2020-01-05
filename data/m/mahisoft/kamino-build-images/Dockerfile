FROM openjdk:8-alpine

RUN apk update && apk add py-pip && rm -rf /tmp/* /var/cache/apk/*
RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-17.03.0-ce.tgz -O /docker.tgz && \
    cd / && \
    tar -xvzf /docker.tgz && \
    mv /docker/* /usr/local/bin && \
    rm /docker.tgz
RUN pip install docker-compose