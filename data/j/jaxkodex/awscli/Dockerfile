FROM alpine:3.10
MAINTAINER colin.hom@coreos.com

RUN apk --no-cache --update add bash curl less groff jq python py-pip && \
  pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir awscli==1.16.249 s3cmd==2.0.0 && \
  mkdir /root/.aws && \
  aws --version && \
  s3cmd --version

ENTRYPOINT []
