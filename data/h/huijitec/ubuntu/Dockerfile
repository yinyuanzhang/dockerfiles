FROM ubuntu:18.04

# 更换镜像
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
  && sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list

ENV TZ="Asia/Shanghai" \
  DEBIAN_FRONTEND=noninteractive
RUN apt-get clean
RUN apt-get update \
  && apt-get install -y \
  ca-certificates \
  apt-transport-https \
  bash \
  tar \
  git \
  openssl \
  curl \
  wget \
  unzip \
  locales \
  tzdata

RUN echo "Asia/Shanghai" > /etc/timezone \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && rm -rf /var/lib/apt/lists/* \
  && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
  && dpkg-reconfigure -f noninteractive tzdata

ENV LANG en_US.utf8
