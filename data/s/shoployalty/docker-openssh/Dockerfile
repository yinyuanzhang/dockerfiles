FROM alpine:latest

LABEL version="1.1"
LABEL description="Обрaаз docker с ипортом ключа rsa"
LABEL maintainer="Aleksey Gulyaev <ag@napoleonit.ru>"

RUN apk add --no-cache \
		ca-certificates

ENV DOCKER_CHANNEL edge
ENV DOCKER_VERSION 17.05.0-ce

RUN set -ex; \
# why we use "curl" instead of "wget":
# + wget -O docker.tgz https://download.docker.com/linux/static/stable/x86_64/docker-17.03.1-ce.tgz
# Connecting to download.docker.com (54.230.87.253:443)
# wget: error getting response: Connection reset by peer
	apk add --no-cache --virtual .fetch-deps \
		curl \
		tar \
	; \
	curl -fL -o docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz"; \
	tar --extract \
		--file docker.tgz \
		--strip-components 1 \
		--directory /usr/local/bin/ \
	; \
	rm docker.tgz; \
	apk del .fetch-deps; \
	dockerd -v; \
	docker -v; \
 	apk add --no-cache \
	 	git \
		openssh-client; \
	git config --global user.email "docker-openssh@gitlab.org"; \
  	git config --global user.name "docker-openssh"; \
  	mkdir -p ~/.ssh; \
  	echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config; \
  	echo -e "Host gitlab.itnap.ru\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config

COPY docker-openssh-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-openssh-entrypoint.sh

ENTRYPOINT ["docker-openssh-entrypoint.sh"]
CMD ["sh"]