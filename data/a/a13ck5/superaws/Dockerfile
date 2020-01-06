FROM alpine:latest

MAINTAINER Alex Dixon <davidadixon@gmail.com>

RUN apk -v --update add \
python \
py-pip \
less \
&& \
pip install --upgrade pip awscli saws && \
mkdir /root/.aws && \
rm /var/cache/apk/*