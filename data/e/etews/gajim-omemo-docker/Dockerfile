FROM debian:unstable

MAINTAINER Erik Tews <erik@datenzone.de>

RUN useradd -m gajim; echo "deb http://deb.debian.org/debian experimental main" > /etc/apt/sources.list.d/experimental.list; apt-get update && apt-get  install -y gajim; apt-get -t experimental -y install gajim-omemo; rm -rf /var/lib/apt/lists/*

COPY start-gajim.sh /tmp/
ENTRYPOINT ["/tmp/start-gajim.sh"]
