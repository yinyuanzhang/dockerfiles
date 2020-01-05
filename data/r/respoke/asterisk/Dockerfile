FROM respoke/pjsip:latest 
MAINTAINER Respoke <info@respoke.io> 

RUN useradd --system asterisk

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
            build-essential \
            curl \
            libcurl4-openssl-dev \
            libedit-dev \
            libgsm1-dev \
            libjansson-dev \
            libogg-dev \
            libsqlite3-dev \
            libsrtp0-dev \
            libssl-dev \
            libxml2-dev \
            libxslt1-dev \
            uuid \
            uuid-dev \
            binutils-dev \
            libpopt-dev \
            libspandsp-dev \
            libvorbis-dev \
            portaudio19-dev \
            python-pip \
            && \
    pip install j2cli && \
    apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*

ENV ASTERISK_VERSION=13.10.0
COPY build-asterisk.sh /build-asterisk
RUN /build-asterisk && rm -f /build-asterisk
COPY asterisk-docker-entrypoint.sh /
CMD ["/usr/sbin/asterisk", "-f"]
ENTRYPOINT ["/asterisk-docker-entrypoint.sh"]
