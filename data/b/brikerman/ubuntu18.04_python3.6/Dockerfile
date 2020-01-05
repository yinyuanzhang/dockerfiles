FROM ubuntu:18.04
MAINTAINER BrikerMan "<https://eliyar.biz>"

RUN sed -i 's/http:\/\/archive\.ubuntu\.com\/ubuntu\//http:\/\/mirrors\.aliyun\.com\/ubuntu\//g' /etc/apt/sources.list

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install python
RUN apt-get -qqy update \
    && apt-get install -qqy --no-install-recommends \
    tzdata language-pack-en-base locales git python3-numpy python3-dev python3-pip python3-wheel python3-setuptools build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

# pip
RUN mkdir  ~/.pip && echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > ~/.pip/pip.conf
RUN pip3 install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
