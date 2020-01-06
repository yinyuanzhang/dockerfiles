# 20191205 Force rebuild 

FROM reisen/debian-arm-qemu 

#AS add-apt-repositories

RUN [ "cross-build-start" ]

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y gnupg \
 && apt-key adv --fetch-keys http://www.webmin.com/jcameron-key.asc \
 && echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list

#RUN [ "cross-build-end" ]

#FROM reisen/debian-arm-qemu

#RUN [ "cross-build-start" ]

LABEL maintainer="jcgaliana@gmail.com"

ENV BIND_USER=bind \
#    BIND_VERSION=9.11.3 \
#    WEBMIN_VERSION=1.9 \
    DATA_DIR=/data

# COPY --from=add-apt-repositories /etc/apt/trusted.gpg /etc/apt/trusted.gpg

# COPY --from=add-apt-repositories /etc/apt/sources.list /etc/apt/sources.list

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
 && apt-get update \
 && apt-get upgrade -y \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      bind9 bind9-host dnsutils \
      webmin \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh

RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 53/udp 53/tcp 10000/tcp

RUN [ "cross-build-end" ]

ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["/usr/sbin/named"]
