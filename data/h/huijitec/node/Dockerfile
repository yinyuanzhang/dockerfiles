FROM node:12-alpine

# 设置镜像
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

ENV TZ="Asia/Shanghai"
RUN apk update \
  && apk add --no-cache --update \
  ca-certificates \
  bash \
  tzdata \
  tar \
  xz \
  bzip2 \
  git \
  openssl \
  curl \
  wget \
  unzip

RUN echo "Asia/Shanghai" > /etc/timezone \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN npm config set registry https://registry.npm.taobao.org \
  && npm config set disturl https://npm.taobao.org/dist \
  && npm config set electron_mirror https://npm.taobao.org/mirrors/electron/ \
  && npm config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/ \
  && npm config set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs/ \
  && yarn config set registry https://registry.npm.taobao.org \
  && yarn config set disturl https://npm.taobao.org/dist \
  && yarn config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/ \
  && yarn config set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs/

RUN npm install gulp-cli -g
