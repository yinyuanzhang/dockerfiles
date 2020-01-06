FROM debian:wheezy

# Configure apt
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

# Install prereqs
RUN apt-get update && \
    apt-get install -y supervisor nginx-light php5-fpm php-apc php5-cli php5-intl php5-gd php5-mysqlnd php-mail curl && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# Set mediawiki version info
ENV MEDIAWIKI_MAJOR 1.23
ENV MEDIAWIKI_VERSION 1.23.7

# Install mediawiki
RUN mkdir /src && cd /src && \
    curl -SL http://download.wikimedia.org/mediawiki/$MEDIAWIKI_MAJOR/mediawiki-$MEDIAWIKI_VERSION.tar.gz -o /src/mediawiki.tgz && \
    tar zxf mediawiki.tgz && rm mediawiki.tgz && \
    mv /src/mediawiki-* /src/mediawiki && \
    cd /src/mediawiki/extensions && \
    curl -SL https://github.com/gilluminate/FancyBoxThumbs/archive/master.tar.gz -o /src/mediawiki/extensions/FancyBoxThumbs.tgz && \
    tar zxf FancyBoxThumbs.tgz && rm FancyBoxThumbs.tgz && mv FancyBoxThumbs-master FancyBoxThumbs && \
    curl -SL "https://git.wikimedia.org/zip/?r=mediawiki/extensions/MultiMaps&h=REL1_23&format=gz" -o /src/mediawiki/extensions/MultiMaps.tgz && \
    mkdir MultiMaps && tar zxf MultiMaps.tgz -C MultiMaps && rm MultiMaps.tgz && \
    chown -R www-data:www-data /src/mediawiki/

# Add system service config
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD ./fpm.conf /etc/php5/fpm/php-fpm.conf
ADD ./fpm-pool-www.conf /etc/php5/fpm/pool.d/www.conf
ADD ./mediawiki-start /usr/bin/mediawiki-start

# Add data directory and symlinks that can then be used as a data volume
RUN mkdir /data && \
    ln -s /data/LocalSettings.php /src/mediawiki/LocalSettings.php && \
    rm -rf /src/mediawiki/images && \
    ln -s /data/images /src/mediawiki/images

# Setup volumes
RUN rm -rf /var/log/**/*.log

# Setup volumes
VOLUME /data
VOLUME /var/log

EXPOSE 80
WORKDIR /src/mediawiki/maintenance
CMD ["/usr/bin/mediawiki-start"]
