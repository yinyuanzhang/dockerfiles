# bash on alpine
#
# VERSION               1.0

FROM alpine:3.8
MAINTAINER Christopher Hunter "mail@chrishunter.me"

RUN apk add --no-cache bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

ENV LC_ALL=en_US.UTF-8
WORKDIR /root
