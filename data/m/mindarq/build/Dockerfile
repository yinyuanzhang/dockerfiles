FROM node:8-stretch

RUN apt-get update && apt-get -y install \
  python3-dev \
  python3-pip \
  && rm -rf /var/lib/apt/lists/* \
  && pip3 install awscli \
  && npm install -g bower