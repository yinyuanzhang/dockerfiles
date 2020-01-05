FROM node:8

MAINTAINER maji-KY

USER root

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list' \
  && apt update \
  && apt install -y google-chrome-stable

