# Dockerfile for the 2.3 GA version of MariaDB MaxScale
FROM ubuntu:bionic

COPY maxscale/maxscale.list /etc/apt/sources.list.d/maxscale.list.tmp

RUN apt-get -y update && \
    apt-get -y install gnupg2 && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "0x135659e928c12247" && \
    mv /etc/apt/sources.list.d/maxscale.list.tmp /etc/apt/sources.list.d/maxscale.list && \
    apt-get -y update && \
    apt-get -y install maxscale && \
    rm -rf /var/lib/apt/lists/*

COPY maxscale/maxscale.cnf /etc/
ENTRYPOINT ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]
RUN mkdir /etc/maxscale
RUN mkdir /etc/maxscale.cnf.d/
COPY maxscale/docker-entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh && \
    ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]
