FROM node:7.4-slim
MAINTAINER Erik Weber <erik@vangenplotz.no>

RUN apt-get update \
    && apt-get install -y git libfontconfig1 bzip2 \
    && npm install -g gulp \
    && npm install -g bower \
    && apt-get clean