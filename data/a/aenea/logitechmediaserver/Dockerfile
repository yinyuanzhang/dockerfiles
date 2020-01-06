FROM phusion/baseimage

MAINTAINER aenea <docker@aenea.org>

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes \
    libgdbm3 \
    libgomp1 \
    libio-socket-ssl-perl \
    locales \
    netbase \
    perl \
    python-meld3 \
    python-pkg-resources \
    rename \
    supervisor && \
    rm -rf /var/lib/apt/lists/*

# Install LMS
ENV LMS_URL="http://www.mysqueezebox.com/update/?version=7.9.1&revision=1&geturl=1&os=deb"
RUN useradd --system --uid 801 -M -s /bin/false -d /usr/share/squeezeboxserver -G nogroup -c "Logitech Media Server user" squeezeboxserver && \
    apt-get update && \
    apt-get install --yes wget && \
    wget $(wget -q -O - "$LMS_URL") -q -O /tmp/lms.deb && \
    dpkg -i /tmp/lms.deb && \
    rm -f /tmp/lms.deb && \
    apt-get -y remove wget && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    dpkg-reconfigure locales

# Make /etc/squeezebox server stateful
RUN mkdir -p /mnt/state/etc && \
    mv /etc/squeezeboxserver /etc/squeezeboxserver.orig && \
    ln -s /mnt/state/etc /etc/squeezeboxserver && \
    cp -pr /etc/squeezeboxserver.orig/* /etc/squeezeboxserver/

# Make /var/lib/squeezeboxserver/cache stateful
RUN mkdir -p /mnt/state/cache && \
    mv /var/lib/squeezeboxserver/cache /var/lib/squeezeboxserver/cache.orig && \
    ln -s /mnt/state/cache /var/lib/squeezeboxserver/cache && \
    chown -R squeezeboxserver.nogroup /var/lib/squeezeboxserver/cache && \
    chown -R squeezeboxserver.nogroup /mnt/state

RUN mkdir -p /var/log/supervisor

COPY ./supervisord.conf /etc/
COPY ./start-lms.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-lms.sh

VOLUME ["/mnt/state", "/mnt/music", "/mnt/playlists"]

EXPOSE 3483 3483/udp 9000 9090 9010

CMD ["/usr/local/bin/start-lms.sh"]
