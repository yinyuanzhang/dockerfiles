FROM alpine:latest


MAINTAINER James Knight <tech@jamesknightcoaching.com>

ENV LANGUAGE=en_US
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US


RUN echo "@edge-community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories


RUN apk --update --no-cache \
  add \
  zlib zlib-dev \
  build-base \
  libxml2 libxml2-dev \
  libxslt libxslt-dev \
  readline readline-dev \
  ruby ruby-dev ruby-io-console ruby-irb \
  ruby-json ruby-rake ruby-rdoc ruby-bigdecimal \
  git bash \
  yaml yaml-dev \
  libffi libffi-dev \
  nodejs-npm  \
  python2 rsync \
  sshpass openssh openssh-client \
  tar automake alpine-sdk nasm autoconf  \
  libpng libpng-dev \
  libwebp libwebp-dev \
  libjpeg-turbo libjpeg-turbo-dev libjpeg-turbo-utils \
  yarn@edge-community \
  gifsicle@edge-community \
  optipng@edge-community

#  && rm /var/cache/apk/*


RUN gem update --system && gem clean && gem install --no-ri --no-rdoc \
  json:1.8.6 nokogiri:1.7.0.1 jekyll:3.8.3

RUN rm -rf /usr/lib/ruby/gems/*/cache/*.gem


RUN yarn global add gulp@4.0.0 gulp-cli@latest



WORKDIR /app
ADD . /app
