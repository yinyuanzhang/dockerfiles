FROM gcr.io/etcd-development/etcd:v3.4.3

ENV TZ="Asia/Shanghai" \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get clean
RUN apt-get update \
  && apt-get install -y \
  apt-utils \
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
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

