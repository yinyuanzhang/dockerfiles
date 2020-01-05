FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get install -y apt-transport-https ca-certificates unzip \
    && apt-get install php-cli php-curl php-intl php-sqlite3 php-mysqli php-xml php-mbstring composer -y
