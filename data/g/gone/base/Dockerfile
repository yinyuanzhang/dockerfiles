FROM gone/phusion:x86
LABEL maintainer="Gone.io <hello@gone.io>"

CMD ["/sbin/my_init"]

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm-256color \
    COMPOSER_ALLOW_SUPERUSER=1 \
    COLOUR_FAIL='\e[31m' \
    COLOUR_SUCCESS='\e[32m' \
    COLOUR_NONE='\e[39m'

RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/force-unsafe-io && \
    apt-get -qq update && \
    apt-get -yq install --no-install-recommends \
        inetutils-ping \
        bash \
        nano \
        host \
        curl \
        wget \
        unzip \
        git \
        ca-certificates \
        tzdata \
        python-software-properties && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    echo Europe/London > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

SHELL ["/bin/bash", "-c"]

RUN mkdir -p /app
WORKDIR /app