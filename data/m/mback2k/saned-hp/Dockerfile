FROM mback2k/ubuntu:bionic

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sane sane-utils libsane libsane-extras libsane-hpaio \
        dbus cups cups-bsd cups-client libcups2 \
        hplip hpijs-ppds printer-driver-gutenprint \
        snmp-mibs-downloader locales supervisor && \
    apt-get clean

RUN locale-gen en_US en_US.UTF-8 && dpkg-reconfigure locales

RUN sed -i 's/^#\s*data_portrange\s*=\s*.*$/data_portrange = 10000 - 10010/g' /etc/sane.d/saned.conf

EXPOSE 6566 10000-10010

ADD docker-entrypoint.d/ /run/docker-entrypoint.d/

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
