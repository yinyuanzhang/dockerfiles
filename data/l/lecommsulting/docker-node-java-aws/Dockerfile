FROM node:12-slim
LABEL maintainer="Daniel Grabert <daniel.grabert@wpi-art.org>"

ENV CHROME_BIN /usr/bin/chromium
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt update 
RUN apt -y dist-upgrade

RUN mkdir -p /usr/share/man/man1

RUN DEBIAN_FRONTEND=noninteractive apt install -y \
    curl \
    chromium \
    default-jre \
    maven \
    git \
    mysql-client \
    python3-pip \
    procps \
    zip

RUN pip3 --no-cache-dir install awscli --upgrade

RUN pip3 --no-cache-dir install awsebcli --upgrade

RUN apt-get -y autoremove

RUN apt-get -y clean

RUN rm -rf /var/lib/apt/lists
