FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y nginx php5-fpm php5-json php5-cli php5-mysql php5-curl unzip git supervisor

RUN git clone git://github.com/pagekit/pagekit.git

RUN chown -R www-data:www-data /pagekit

WORKDIR /pagekit

RUN php -r "readfile('https://getcomposer.org/installer');" | php
RUN php ./composer.phar install

# debug tools after composer so it does not fuck up the cache too much
# RUN apt-get install -y vim procps screen net-tools mysql-client && \
#    apt-get clean
# RUN echo "shell /bin/bash" >> /etc/screenrc

COPY vhost.conf /etc/nginx/sites-enabled/default
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf

RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

ADD init.sh /init.sh

VOLUME ["/pagekit/storage", "/pagekit/app/cache"]

EXPOSE 80

CMD ["/init.sh"]