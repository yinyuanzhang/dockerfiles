FROM debian:wheezy

# Configure apt
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

# Install prereqs
RUN apt-get update && \
    apt-get install -y supervisor nginx-full php5-fpm php-apc php5-cli php5-intl php5-gd php5-mysqlnd php5-curl php-mail curl bzip2 imagemagick && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# Set phpbb version info
ENV PHPBB_VERSION 3.1.10
ENV PHPBB_ROOT /usr/share/phpbb
ENV PHPBB_DEFAULTS /usr/share/phpbb-defaults

# Install phpbb
RUN cd /root/ && \
    curl -SL https://www.phpbb.com/files/release/phpBB-$PHPBB_VERSION.tar.bz2 -o /root/phpbb.tar.bz2 && \
    tar jxf phpbb.tar.bz2 && rm phpbb.tar.bz2 && \
    mv phpBB3 $PHPBB_ROOT && \
    mkdir $PHPBB_DEFAULTS && \
    mv $PHPBB_ROOT/config     $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/ext        $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/files      $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/images     $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/language   $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/styles     $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/store      $PHPBB_DEFAULTS/ && \
    mv $PHPBB_ROOT/config.php $PHPBB_DEFAULTS/ && \
    chown -R www-data:www-data $PHPBB_ROOT/ $PHPBB_DEFAULTS/

# Add system service config
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD ./fpm.conf /etc/php5/fpm/php-fpm.conf
ADD ./fpm-pool-www.conf /etc/php5/fpm/pool.d/www.conf
ADD ./phpbb-start /usr/bin/phpbb-start

# Setup volumes
RUN rm -rf /var/log/**/*.log

# Setup volumes
VOLUME /var/log
VOLUME $PHPBB_ROOT/config
VOLUME $PHPBB_ROOT/ext
VOLUME $PHPBB_ROOT/files
VOLUME $PHPBB_ROOT/images
VOLUME $PHPBB_ROOT/language
VOLUME $PHPBB_ROOT/styles
VOLUME $PHPBB_ROOT/store

EXPOSE 80
WORKDIR $PHPBB_ROOT
CMD ["/usr/bin/phpbb-start"]
