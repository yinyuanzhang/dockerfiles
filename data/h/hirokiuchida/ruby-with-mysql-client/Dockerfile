FROM ruby:2.4.1

MAINTAINER Hiroki Uchida <info@hiroki-uchida.com>

RUN apt-get clean && apt-get update && apt-get install mysql-client locales -y

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN locale-gen ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
