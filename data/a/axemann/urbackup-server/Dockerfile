FROM debian:stretch
MAINTAINER Martin Raiber <martin@urbackup.org>

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y gnupg &&\
    echo 'deb http://download.opensuse.org/repositories/home:/uroni/Debian_9.0/ /' > /etc/apt/sources.list.d/urbackup-server.list &&\
    apt-key adv --fetch-keys http://download.opensuse.org/repositories/home:/uroni/Debian_9.0/Release.key &&\
    apt-get update &&\
    echo "urbackup-server urbackup/backuppath string /backups" | debconf-set-selections &&\
    export DEBIAN_FRONTEND=noninteractive &&\
    apt-get install -y --no-install-recommends --allow-unauthenticated urbackup-server btrfs-tools &&\
    rm -rf /var/lib/apt/lists/*

COPY start /usr/bin/start

EXPOSE 55413/tcp 55414/tcp 55415/tcp 35623/udp

VOLUME [ "/backups", "/var/urbackup", "/var/log", "/usr/share/urbackup" ]
ENTRYPOINT ["/usr/bin/start"]
CMD ["run"]