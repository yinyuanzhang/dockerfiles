FROM node:8.10-alpine
MAINTAINER Hardys <hardyscc@gmail.com>

RUN apk add --no-cache \
    python \
    py-pip \
    ca-certificates \
    groff \
    less \
    bash \
  && pip install --no-cache-dir --upgrade pip awscli

RUN npm -g install npm serverless@1.41.1

WORKDIR /root
CMD bash
