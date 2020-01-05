# Download base image
FROM debian:stretch

# Define the ARG variables
ARG VERSION
ARG BUILD_DATE
ARG VCS_REF
ARG OVERLAY_VERSION=v1.21.4.0
ARG OVERLAY_ARCH=amd64

# Labels
LABEL org.label-schema.name="Debian base docker image" \
      org.label-schema.description="This is a Debian base docker image with s6-overlay" \
      org.label-schema.vendor="Paul NOBECOURT <paul.nobecourt@orange.fr>" \
      org.label-schema.url="https://github.com/pnobecourt/" \
      org.label-schema.version=$VERSION \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/pnobecourt/docker-debian-s6" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0"

# Define the ENV variables
ENV LANG=C.UTF-8 \
DEBIAN_FRONTEND=noninteractive \
SHELL=/bin/bash \
TERM=xterm \
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
PS1=$(whoami)@$(hostname):$(pwd)$

# Install tools and s6-overlay
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    apt-transport-https \
                    apt-utils \
                    bash \
                    bash-completion \
                    ca-certificates \
                    coreutils \
                    curl \
                    dirmngr \
                    gnupg \
                    less \
                    logrotate \
                    nano \
                    net-tools \
                    passwd \
                    procps \
                    sudo \
                    tzdata \
                    wget \
                    && \
    curl -L -S https://github.com/just-containers/s6-overlay/releases/download/$OVERLAY_VERSION/s6-overlay-$OVERLAY_ARCH.tar.gz | tar xvz -C / && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf \
           /tmp/* \
           /var/lib/apt/lists/* \
           /var/log/* \
           /var/tmp/*

# Add files
ADD /root /

# Entrypoint
ENTRYPOINT [ "/init" ]
