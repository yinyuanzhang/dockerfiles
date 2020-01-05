FROM alpine

ENV DOCKER_VERSION=18.09.6 DOCKER_COMPOSE_VERSION=1.24.0 GLIBC_VERSION=2.29-r0

COPY ca-certificates /usr/local/share/ca-certificates/
RUN apk update \
 && apk add  \
    bash \
    bash-completion \
    ca-certificates \
    coreutils \
    curl \
    git \
    less \
    openssh-client \
    vim
WORKDIR /root
COPY root/ /root

# Install glibc, Docker, and Docker Compose
RUN set -x \
 && curl -sSL -o /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
 && curl -sSL -O "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \
 && curl -sSL -O "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" \
 && apk add glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk \
 && rm glibc*.apk \
 && curl -sSL "https://download.docker.com/linux/static/stable/$(uname -m)/docker-$DOCKER_VERSION.tgz" -o docker.tgz \
 && tar -xzvf docker.tgz \
 && mv docker/docker /usr/local/bin/ \
 && rm -rf docker \
 && rm docker.tgz \
 && docker -v \
 && curl -sSL "https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m`" -o /usr/local/bin/docker-compose \
 && chmod +x /usr/local/bin/docker-compose \
 && docker-compose -v \
 && curl -sSL https://github.com/docker/cli/raw/master/contrib/completion/bash/docker -o /usr/share/bash-completion/completions/docker \
 && curl -sSL https://github.com/docker/compose/raw/master/contrib/completion/bash/docker-compose -o /usr/share/bash-completion/completions/docker-compose

CMD ["/bin/bash"]
