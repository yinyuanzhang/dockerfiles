FROM golang:1.12.7-alpine3.10
MAINTAINER kateinoigakukun

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 19.03.0
ENV COMPOSE_VERSION 1.24.1

WORKDIR /elypod
RUN apk --update add git less openssh py-pip python-dev libffi-dev openssl-dev gcc libc-dev make && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN set -eux; \
	\
# this "case" statement is generated via "update.sh"
	apkArch="$(apk --print-arch)"; \
	case "$apkArch" in \
# amd64
		x86_64) dockerArch='x86_64' ;; \
# arm32v6
		armhf) dockerArch='armel' ;; \
# arm32v7
		armv7) dockerArch='armhf' ;; \
# arm64v8
		aarch64) dockerArch='aarch64' ;; \
		*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\
	esac; \
	\
	if ! wget -O docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz"; then \
		echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${dockerArch}'"; \
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
RUN pip install "docker-compose${COMPOSE_VERSION:+==}${COMPOSE_VERSION}"

RUN go get github.com/bketelsen/captainhook
RUN mkdir -p $HOME/.ssh && \
    chmod 0700 $HOME/.ssh && \
    ssh-keyscan github.com > $HOME/.ssh/known_hosts
COPY ssh/config /root/.ssh/config
ADD webhooks /elypod/webhooks
ADD scripts /elypod/scripts

EXPOSE 80
CMD ["/go/bin/captainhook", "-listen-addr=0.0.0.0:80", "-configdir=/elypod/webhooks"]
