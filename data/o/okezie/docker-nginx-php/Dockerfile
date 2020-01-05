FROM phusion/baseimage:0.10.0

# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

ENV HOME /root

RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]

# Nginx-PHP Installation
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y vim curl wget build-essential python-software-properties
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y --force-yes php7.0-cli php7.0-fpm php7.0-mysql php7.0-pgsql php7.0-sqlite php7.0-curl\
	php7.0-gd php7.0-mcrypt php7.0-intl php7.0-imap php7.0-tidy

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.0/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.0/cli/php.ini

RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini

RUN mkdir -p        /var/www /run/php/ /etc/service/phpfpm 
ADD build/default   /etc/nginx/sites-available/default
ADD build/nginx.sh  /etc/service/nginx/run
ADD build/phpfpm.sh /etc/service/phpfpm/run
RUN chmod +x        /etc/service/nginx/run /etc/service/phpfpm/run        
# End Nginx-PHP

RUN apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80 443
