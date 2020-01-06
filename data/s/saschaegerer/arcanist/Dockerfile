FROM saschaegerer/php-fpm:7.2

USER root

# install required package git
RUN set -xe && \
    apt-get update && \
    apt-get install --no-install-recommends -y git php7.2-curl && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDependencies && \
    rm -rf /var/lib/apt/lists/*

# install arcanist
RUN mkdir /opt/arcanist && \
	cd /opt/arcanist && \
	git clone https://github.com/phacility/libphutil.git && \
	git clone https://github.com/phacility/arcanist.git && \
	ln -s /opt/arcanist/arcanist/bin/arc /usr/local/bin/

USER www-data

# unset the entrypoint of parent image
ENTRYPOINT [""]

CMD ["arc", "help"]
