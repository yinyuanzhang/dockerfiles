# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

FROM alpine:3.9.3
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

# Environment variables
ENV USER prod
ENV HOME /home/${USER}

# Install various tools
RUN export DEBIAN_FRONTEND=noninteractive \
  && apk add \
       bash \
       ca-certificates \
       coreutils \
       curl \
       iproute2 \
       iputils \
       less \
       netcat-openbsd \
       net-tools \
       shadow \
       strace \
       tcpdump \
       unzip \
       wget \
  && rm -rf /var/cache/apk/*

# Install dumb-init
RUN wget -nv https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 -O /usr/bin/dumb-init \
    && echo "81231da1cd074fdc81af62789fead8641ef3f24b6b07366a1c34e5b059faf363  /usr/bin/dumb-init" \
        | sha256sum - \
    && chmod +x /usr/bin/dumb-init

# Install grpc-health-probe
RUN wget -nv -O /usr/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/v0.1.0-alpha.1/grpc_health_probe-linux-amd64 \
    && echo "0f8c0cefbadfd68e294809cac7ed7981e0bb78ba1c15edd1da21e4d34d1944f0  /usr/bin/grpc_health_probe" \
        | sha256sum -c - \
    && chmod +x /usr/bin/grpc_health_probe

# Create the user and move into $HOME
RUN useradd -m ${USER} -u 1000
WORKDIR ${HOME}

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
