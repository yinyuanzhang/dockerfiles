FROM qoopido/base:latest
MAINTAINER Dirk Lüth <info@qoopido.com>

# Initialize environment
	CMD ["/sbin/my_init"]
	ENV DEBIAN_FRONTEND noninteractive

# configure defaults
	COPY configure.sh /
	ADD config /config
	RUN chmod +x /configure.sh \
		&& chmod 755 /configure.sh
	RUN /configure.sh \
		&& chmod +x /etc/my_init.d/*.sh \
		&& chmod 755 /etc/my_init.d/*.sh \
		&& chmod +x /etc/service/memcached/run \
		&& chmod 755 /etc/service/memcached/run
	
# install packages
	RUN apt-get update \
		&& apt-get install -qy memcached

# add default /app directory
	RUN mkdir -p /app/data/logs

# cleanup
	RUN apt-get -qy autoremove \
		&& deborphan | xargs apt-get -qy remove --purge \
		&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /usr/share/doc/* /usr/share/man/* /tmp/* /var/tmp/* /configure.sh \
		&& find /var/log -type f -name '*.gz' -exec rm {} + \
		&& find /var/log -type f -exec truncate -s 0 {} +

# finalize
	VOLUME ["/app/data"]
	EXPOSE 11211
