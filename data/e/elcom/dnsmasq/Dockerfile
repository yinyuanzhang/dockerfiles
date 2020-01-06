FROM debian:stretch
MAINTAINER LWB

ENV ADBLOCK_URL_LIST=http://pgl.yoyo.org/adservers/serverlist.php?hostformat=nohtml&showintro=1 \
		WHITE_LIST="" \
		EXTRA_LIST="" \
		TARGET_IP=127.0.0.1

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --force-yes --no-install-recommends dnsmasq wget ca-certificates && \
    service dnsmasq stop && \
    rm -rf /var/lib/apt/lists

EXPOSE 53 53/udp

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["dnsmasq", "--no-daemon"]
