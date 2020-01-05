FROM debian:stretch-backports

RUN apt-get update && apt-get -y dist-upgrade && \
    apt-get install -yt stretch-backports tor curl && \
    curl -sSL https://git.io/get-mo -o /usr/local/bin/mo && chmod +x /usr/local/bin/mo && \
    apt-get -y purge curl && apt-get -y autoremove --purge && \
    rm -rf /var/{lib,log,cache}/apt

VOLUME ["/srv/data"]

ENTRYPOINT ["/srv/docker-entrypoint.sh"]

CMD ["tor", "-f", "/etc/tor/torrc"]

ADD . /srv/
