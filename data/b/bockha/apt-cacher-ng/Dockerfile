FROM ubuntu

LABEL maintainer="Hans-Peter.Bock@trumpf.com"
LABEL Version="1.0.0"
LABEL Name="apt-cacher-ng for NAS"

ENV APT_CACHER_NG_VERSION=3.1 \
    APT_CACHER_NG_CACHE_DIR=/var/cache/apt-cacher-ng \
    APT_CACHER_NG_LOG_DIR=/var/log/apt-cacher-ng \
    APT_CACHER_NG_USER=apt-cacher-ng

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
      apt-cacher-ng=${APT_CACHER_NG_VERSION}* ca-certificates \
      avahi-daemon \
 && apt-get clean \
 && sed 's/# ForeGround: 0/ForeGround: 1/' -i /etc/apt-cacher-ng/acng.conf \
 && sed 's/# PassThroughPattern:.*this would allow.*/PassThroughPattern: .* #/' -i /etc/apt-cacher-ng/acng.conf \
 && sed 's/#enable-dbus=yes/enable-dbus=no/' -i /etc/avahi/avahi-daemon.conf \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh

RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 3142/tcp

ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["/usr/sbin/apt-cacher-ng"]
