FROM ubuntu:18.04
MAINTAINER kuri.megane <kuri.megane3060.4@gmail.com>

# apt update
RUN apt update --fix-missing

# set language
RUN apt install -y language-pack-ja
ENV LANG=ja_JP.UTF-8 LC_ALL=ja_JP.UTF-8

# install packages
RUN apt install -y libfontconfig
RUN apt install -y nodejs npm
RUN apt install -y fonts-takao fonts-ipafont fonts-ipaexfont fonts-noto-cjk 

# update all other packages
RUN apt upgrade -y

# cache clean
RUN apt clean

# node.js の環境変数
ENV NODE_ENV=dev
ENV NODE_PATH=/usr/local/lib/node_modules

# markdown-pdf
RUN npm install -g markdown-pdf
WORKDIR /markdown-pdf
COPY markdown.css .
COPY convert.js .

# gitbook
RUN npm install -g gitbook-cli

# 作業ディレクトリ
WORKDIR /app

# ポート開放
EXPOSE 4000