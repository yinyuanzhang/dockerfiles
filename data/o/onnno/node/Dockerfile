FROM onnno/ubuntu:16.04

MAINTAINER Dong Li "docker@lidong.me”

ENV NODE_VERSION 6.13.1

RUN  apt-get update \
	&& apt-get install -y --no-install-recommends xz-utils \
	&& apt-get autoremove

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

CMD ["node"]
