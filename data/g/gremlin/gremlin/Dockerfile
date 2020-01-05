FROM ubuntu:18.04

MAINTAINER Gremlin Inc. <support@gremlin.com>

ENV DEBIAN_FRONTEND noninteractive

ENV SERVICE_URL          https://api.staging.gremlin.com/v1
ENV CLIENT_VERSION       latest
ENV DAEMON_VERSION       latest
ENV GREMLIN_DOCKER_IMAGE gremlin/gremlin:staging

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y ca-certificates gnupg2 apt-transport-https \
    && echo "deb https://deb.gremlin.com/ staging non-free" > /etc/apt/sources.list.d/gremlin.list \
    && echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E15DED2F B302C012 2C52609D 61A50EF6 \
    && apt-get update \
    && apt-get install -y sudo dnsutils iproute2 docker-engine lsb-core \
    # HACK to work around install scripts, we only need the binaries
    && apt-get install -y -d gremlin gremlind \
    && mkdir /tmp/gremlin \
    && dpkg -x /var/cache/apt/archives/gremlin_*.deb /tmp/gremlin \
    && dpkg -x /var/cache/apt/archives/gremlind_*.deb /tmp/gremlin \
    && cp -a /tmp/gremlin/usr/bin/gremlin /usr/bin/gremlin \
    && cp -a /tmp/gremlin/usr/sbin/gremlind /usr/sbin/ \
    && rm -rf /tmp/gremlin /var/cache/apt/archives/gremlin*.deb /var/lib/apt/lists/*

COPY entrypoints/main.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
