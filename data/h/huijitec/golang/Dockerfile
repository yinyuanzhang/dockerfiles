FROM golang:1-alpine

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

################################################################################
# 安装golang.org公用库

RUN go get -u -v golang.org/x/crypto/... \
    && go get -u -v golang.org/x/image/... \
    && go get -u -v golang.org/x/net/... \
    && go get -u -v golang.org/x/sync/... \
    && go get -u -v golang.org/x/sys/... \
    && go get -u -v golang.org/x/text/... \
    && go get -u -v golang.org/x/time/... \
    && go get -u -v golang.org/x/tools/... \
    && go get -u -v golang.org/x/xerrors/...
