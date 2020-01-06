FROM ubuntu:18.04

LABEL maintainer="Łukasz Górski <l.gorski@trojmiasto.pl>"

RUN apt-get update \
      && apt-get install -y \
        software-properties-common \
        unzip \
        curl \
        apt-transport-https \
      && apt-key adv --fetch-keys https://pkg.trojmiasto.pl/public.key \
      && echo 'deb [arch=amd64] https://pkg.trojmiasto.pl/ xenial main' > /etc/apt/sources.list.d/pkg-trojmiasto-pl.list \
      && apt-get update \
      && apt install -y \
        ripgrep \
        jq \
        netcat-openbsd \
      && rm -r /var/lib/apt/lists/* \
      && rm -r /var/cache/apt/archives/*

ADD ajax-count /usr/local/bin/ajax-count

SHELL ["/bin/bash", "-c"]

ENTRYPOINT ["/usr/local/bin/ajax-count"]
