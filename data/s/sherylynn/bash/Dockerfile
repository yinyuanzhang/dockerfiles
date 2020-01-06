# Pull base image.
FROM alpine
MAINTAINER Sherylynn <352281674@qq.com>

# install openssl and the complete wget
RUN apk --update add --no-cache bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

ENV LANG zh_CN.UTF-8
