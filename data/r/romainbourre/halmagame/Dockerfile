FROM debian:latest

RUN apt-get update && \
    apt-get install -y \
    gcc \
    make \

COPY . /tmp/app
WORKDIR /tmp/app

