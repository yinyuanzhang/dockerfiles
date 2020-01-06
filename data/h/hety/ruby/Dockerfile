FROM ruby:alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.cloud.tencent.com/' /etc/apk/repositories && sed -i 's/http:/https:/' /etc/apk/repositories && gem sources --add https://mirrors.cloud.tencent.com/rubygems/ --remove https://rubygems.org/ && bundle config mirror.https://rubygems.org https://mirrors.cloud.tencent.com/rubygems
