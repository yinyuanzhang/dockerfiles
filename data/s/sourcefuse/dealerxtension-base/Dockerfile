FROM sourcefuse/dealerxtension:v2

MAINTAINER Rahul Sharma <rahul.sharma@sourcefuse.com>

RUN curl -O https://files.magerun.net/n98-magerun2.phar \
	&& chmod +x ./n98-magerun2.phar \
	&& mv ./n98-magerun2.phar /usr/local/bin/ \
    && mv /usr/local/bin/n98-magerun2.phar  /usr/local/bin/m2

Run apt-get remove --auto-remove php-xdebug -y
RUN  apt-get remove php* -y && apt-get autoremove php* -y  && apt-get purge php* -y
RUN apt-get update -y
RUN apt install php7.2-common php7.2-cli php7.2-fpm php7.2-opcache php7.2-gd php7.2-mysql php7.2-curl php7.2-intl php7.2-xsl php7.2-mbstring php7.2-zip php7.2-bcmath php7.2-soap -y
RUN rm -rf /etc/supervisor/conf.d/supervisord.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]

