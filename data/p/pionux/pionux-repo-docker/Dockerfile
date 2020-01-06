FROM debian:stretch-slim

MAINTAINER hongsea119@gmail.com

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /pionux-mirror \
        && chmod a+rw /pionux-mirror

RUN printf "path-exclude=/usr/share/locale/*\npath-exclude=/usr/share/man/*\npath-exclude=/usr/share/doc/*\npath-include=/usr/share/doc/*/copyright\n" >/etc/dpkg/dpkg.cfg.d/01_nodoc \
	&& mkdir -p /usr/share/man/man1 \
	&& apt-get update \
	&& apt-get -y upgrade \
	&& apt-get -y dist-upgrade \
	&& apt-get install -y --no-install-recommends \
		rsync \
	&& apt-get -y autoremove --purge \
	&& apt-get clean \
	&& rm -rf /var/lib/{apt,dpkg}/

EXPOSE 8873

ADD ./rsyncd.conf /etc/rsyncd.conf
ADD ./run.sh /usr/local/bin/run.sh

USER nobody
ENTRYPOINT ["/usr/local/bin/run.sh"]
