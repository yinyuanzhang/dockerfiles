FROM node:6.10.0


# Install docker
# FROM docker:17.03.0

RUN apt-get -y --fix-missing update \
  && apt-get -y install \
    ca-certificates \
    curl \
    openssl \
    python-setuptools \
    python-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 17.03.0-ce
ENV DOCKER_SHA256 4a9766d99c6818b2d54dc302db3c9f7b352ad0a80a2dc179ec164a3ba29c2d3e

RUN set -x \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v

COPY docker-entrypoint.sh /usr/local/bin/


# Install docker-compose

RUN easy_install pip && pip install docker-compose


# Set node as default command

CMD [ "node" ]
