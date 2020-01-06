FROM node:8-alpine

RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' > /etc/nsswitch.conf

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 18.09.2
ENV DOCKER_COMPOSE_VER 1.23.2
ENV ARCH x86_64

RUN set -eux; \
    echo 'http://nl.alpinelinux.org/alpine/edge/testing' | tee -a /etc/apk/repositories && \
    apk add --no-cache aws-cli bash curl py3-pip git openssh-client

RUN set -eux; \
	if ! wget -O docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${ARCH}/docker-${DOCKER_VERSION}.tgz"; then \
		echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${ARCH}'"; \
		exit 1; \
	fi; \
	\
	tar --extract \
		--file docker.tgz \
		--strip-components 1 \
		--directory /usr/local/bin/ \
	; \
	rm docker.tgz; \
	\
	dockerd --version; \
	docker --version

RUN pip3 install docker-compose && \
    docker-compose --version
