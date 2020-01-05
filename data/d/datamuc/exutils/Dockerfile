FROM alpine:3.10.3
MAINTAINER datamuc
RUN apk add \
    apache2-utils \
    bash \
    bash-completion \
    bind-tools \
    busybox \
    busybox-extras \
    coreutils \
    curl \
    jq \
    netcat-openbsd \
    openssl \
    py3-yaml \
    python3 \
    screen \
    socat \
    tinyproxy \
    vim \
    wget \
    && mkdir /user \
    && sed -i 's/^Allow/#Allow/' /etc/tinyproxy/tinyproxy.conf
COPY assets/bashrc /user/.bashrc
COPY assets/digrc /user/.digrc
RUN chown -R root:root /user && chmod -R g+w /user
ENV HOME /user
ENV SHELL /bin/bash
WORKDIR /user
ENTRYPOINT /bin/bash
