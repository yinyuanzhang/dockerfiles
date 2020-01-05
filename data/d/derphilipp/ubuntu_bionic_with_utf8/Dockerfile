FROM amd64/ubuntu:bionic

RUN echo 'Dir::Cache "";' > /etc/apt/apt.conf.d/02nocache && \
    echo 'Dir::Cache::archives "";' >> /etc/apt/apt.conf.d/02nocache && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive  apt-get -y install --no-install-recommends \
        locales && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apt/archives && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8
