FROM ubuntu:bionic AS add-apt-repositories

RUN apt-get update \
     && DEBIAN_FRONTEND=noninteractive apt-get install -y gnupg \
     && apt-key adv --fetch-keys http://www.webmin.com/jcameron-key.asc \
     && echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list

RUN sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list

FROM ubuntu:bionic

LABEL maintainer="Doino Gretchenliev"

ENV BIND_USER=bind \
     BIND_VERSION=9.11.3 \
     WEBMIN_VERSION=1.9 \
     DATA_DIR=/data \
     BIND_LISTEN_PORT=53

COPY --from=add-apt-repositories /etc/apt/trusted.gpg /etc/apt/trusted.gpg
COPY --from=add-apt-repositories /etc/apt/sources.list /etc/apt/sources.list

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get -y build-dep pam

#Rebuild and istall libpam with --disable-audit option
RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam && dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb libpam0g*.deb
RUN echo exit 0 > /usr/sbin/policy-rc.d

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
     && apt-get purge apt-show-versions \
     && rm /var/lib/apt/lists/*lz4 \
     && apt-get -o Acquire::GzipIndexes=false update \
     && apt-get update \
     && DEBIAN_FRONTEND=noninteractive apt-get install -y \
     bind9=1:${BIND_VERSION}* bind9-host=1:${BIND_VERSION}* dnsutils \
     webmin=${WEBMIN_VERSION}* \
     && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh

RUN chmod 755 /sbin/entrypoint.sh

EXPOSE ${BIND_LISTEN_PORT}/udp ${BIND_LISTEN_PORT}/tcp 10000/tcp

ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["/usr/sbin/named"]
