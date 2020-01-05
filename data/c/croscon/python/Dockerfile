FROM python:2-alpine

RUN apk add --update --no-cache openssl \
  && cd / \
  && wget "https://github.com/croscon/alpine/archive/master.zip" \
  && unzip master.zip \
  && mv alpine-master/tpl / \
  && mv alpine-master/run_tests.sh / \
  && rm -rf master.zip \
  && rm -rf alpine-master


