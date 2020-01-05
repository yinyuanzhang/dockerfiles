FROM haproxy:2.0.6-alpine

RUN apk add --no-cache bash

ENV DOCKER_GEN_VERSION 0.7.4
RUN wget --quiet https://github.com/jwilder/docker-gen/releases/download/${DOCKER_GEN_VERSION}/docker-gen-alpine-linux-amd64-${DOCKER_GEN_VERSION}.tar.gz \
	&& tar -C /usr/local/bin -xvzf docker-gen-alpine-linux-amd64-${DOCKER_GEN_VERSION}.tar.gz \
	&& rm /docker-gen-alpine-linux-amd64-${DOCKER_GEN_VERSION}.tar.gz

RUN wget --quiet https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz \
	&& tar -C /usr/local/bin -xvzf forego-stable-linux-amd64.tgz \
	&& rm forego-stable-linux-amd64.tgz

WORKDIR /usr/src/app
COPY Procfile .
COPY haproxy.tmpl .

CMD ["forego", "start", "-r"]
