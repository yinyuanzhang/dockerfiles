FROM phusion/baseimage:0.9.22

ENV TZ=UTC
EXPOSE 42217

RUN	apt-get update && \
	apt-get -yq purge openssh-.* && \
	apt-get -yq autoremove --purge && \
	apt-get -yq dist-upgrade && \
	apt-get -yq install --no-install-recommends \
		rrdcached

RUN	useradd rrdcached -d /opt/rrdcached -r -m && \
	apt-get -yq autoremove --purge && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD	files /
RUN	chmod -R +x /etc/my_init.d /etc/service && \
	find /opt/rrdcached \( ! -user rrdcached -o ! -group rrdcached \) -exec chown rrdcached:rrdcached {} \;

VOLUME	["/opt/rrdcached/rrd"]
