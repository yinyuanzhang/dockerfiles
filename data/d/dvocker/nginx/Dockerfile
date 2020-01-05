FROM dvocker/ubuntu

MAINTAINER vladimir@drizheruk.com.ua

RUN cd /tmp/ && wget http://nginx.org/keys/nginx_signing.key && sudo apt-key add nginx_signing.key

RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>  /etc/apt/sources.list.d/nginx.list
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >> /etc/apt/sources.list.d/nginx.list

RUN apt-get update
RUN apt-get install nginx

RUN apt-get install -y language-pack-en-base software-properties-common
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php5-5.6
RUN apt-get update
RUN apt-get install -y php5 php5-cli php5-fpm php5-gd php5-json php5-mysql php5-readline php5-curl php5-intl \
php5-mcrypt php5-xmlrpc php5-xsl php5-json
RUN php5enmod mcrypt

COPY etc/ etc/
COPY opt/ opt/
RUN chmod a+x /opt/bin/php56-fpm.wrap

RUN apt-get clean autoclean
RUN apt-get autoremove -y
RUN rm -rf /var/lib/{apt,cache,log}/
RUN rm -rf /tmp/nginx_signing.key

RUN mkdir -p /var/www
RUN chown -R www-data:www-data /var/www/
VOLUME /var/www

EXPOSE 80
