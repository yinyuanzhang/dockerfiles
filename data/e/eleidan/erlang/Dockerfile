FROM eleidan/base:ubuntu-16.04

LABEL maintainer="Oleg Kulyk" \
      description="Erlang/OTP 22.1.6 based on Ubuntu 16.04" \
      init="docker run -it --rm --user $(id -u) -v $(pwd):/home/phantom/app eleidan/erlang:22.1.6-ubuntu-16.04 docker-init.sh" \
      run="docker run -it --rm --user $(id -u) -v $(pwd):/home/phantom/app eleidan/erlang:22.1.6-ubuntu-16.04" \
      version="2019-11-11"

WORKDIR $HOME/app

USER root

COPY docker-init.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-init.sh

# Erlang
ARG OTP_VERSION="22.1.6"
RUN set -xe \
    && apt-get update \
    && runtimeDeps='\
        libsctp1 \
        libwxbase3.0-0v5 \
        libwxgtk3.0-0v5' \
    && apt-get install -y --no-install-recommends $runtimeDeps \
    && wget https://packages.erlang-solutions.com/erlang/debian/pool/esl-erlang_${OTP_VERSION}-1~ubuntu~xenial_amd64.deb -O /tmp/erlang.deb \
    && dpkg -i /tmp/erlang.deb \
    && rm /tmp/erlang.deb \
    && rm -rf /var/lib/apt/lists/*

# rebar
ARG REBAR_VERSION="2.6.4"
RUN set -xe \
    && REBAR_DOWNLOAD_URL="https://github.com/rebar/rebar/archive/${REBAR_VERSION}.tar.gz" \
    && REBAR_DOWNLOAD_SHA256="577246bafa2eb2b2c3f1d0c157408650446884555bf87901508ce71d5cc0bd07" \
    && mkdir -p /usr/src/rebar-src \
    && curl -fSL -o rebar-src.tar.gz "$REBAR_DOWNLOAD_URL" \
    && echo "$REBAR_DOWNLOAD_SHA256 rebar-src.tar.gz" | sha256sum -c - \
    && tar -xzf rebar-src.tar.gz -C /usr/src/rebar-src --strip-components=1 \
    && rm rebar-src.tar.gz \
    && cd /usr/src/rebar-src \
    && ./bootstrap \
    && install -v ./rebar /usr/local/bin/ \
    && rm -rf /usr/src/rebar-src

# rebar3
ARG REBAR3_VERSION="3.12.0"
RUN set -xe \
    && REBAR3_DOWNLOAD_URL="https://github.com/erlang/rebar3/archive/${REBAR3_VERSION}.tar.gz" \
    && REBAR3_DOWNLOAD_SHA256="8ac45498f03e293bc6342ec431888f9a81a4fb9e1177a69965238d127c00a79e" \
    && mkdir -p /usr/src/rebar3-src \
    && curl -fSL -o rebar3-src.tar.gz "$REBAR3_DOWNLOAD_URL" \
    && echo "$REBAR3_DOWNLOAD_SHA256 rebar3-src.tar.gz" | sha256sum -c - \
    && tar -xzf rebar3-src.tar.gz -C /usr/src/rebar3-src --strip-components=1 \
    && rm rebar3-src.tar.gz \
    && cd /usr/src/rebar3-src \
    && HOME=$PWD ./bootstrap \
    && install -v ./rebar3 /usr/local/bin/ \
    && rm -rf /usr/src/rebar3-src

### Needed for the docker-init.sh script
COPY --chown=phantom:phantom recipes $HOME/recipes

ENV SERVICE_NAME="Erlang/OTP ${OTP_VERSION} based on Ubuntu 16.04" \
    USER=${CONTAINER_USER}
