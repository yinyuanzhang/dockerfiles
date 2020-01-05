FROM node:8.4.0-alpine
MAINTAINER kse201 <kse.201@gmail.com>

ARG http_proxy
ARG https_proxy

ENV http_proxy=${http_proxy}
ENV https_proxy=${https_proxy}
ENV HTTP_PROXY=${http_proxy}
ENV HTTPS_PROXY=${https_proxy}

RUN apk update -y && \
    apk add --no-cache redis

ADD ./ /hubot
WORKDIR "/hubot"
VOLUME ["/hubot/conf", "/hubot/scripts"]

ENTRYPOINT ["./bin/run-hubot"]
