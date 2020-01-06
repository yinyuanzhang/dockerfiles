FROM hhvm/hhvm

MAINTAINER "Andrew Vityuk" <andruwa13@me.com>

RUN apt-get clean && apt-get update &&  apt-get upgrade -y

### Cleanup ###
RUN  apt-get autoremove && \
     apt-get autoclean && \
     apt-get clean && \
     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
     
RUN mkdir /var/www/ && \
	chown -R www-data:www-data /var/www/
	
USER www-data

COPY php.ini /etc/hhvm/php.ini

EXPOSE 9000

CMD ["hhvm", "--mode=server"]