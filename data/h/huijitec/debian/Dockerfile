FROM debian:stretch-slim

# 更换镜像
RUN sed -i s@/deb.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list

ENV TZ="Asia/Shanghai" \
  DEBIAN_FRONTEND=noninteractive
RUN apt-get clean
RUN apt-get update \
  && apt-get install -y \
  ca-certificates \
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
