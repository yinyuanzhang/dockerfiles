FROM alpine:3.10

# 设置源镜像
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
