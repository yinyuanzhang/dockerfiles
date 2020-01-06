FROM unilynx/phusion-baseimage-1804

MAINTAINER BeRepublic

ENV DEBIAN_FRONTEND noninteractive
ENV COMPOSER_DISABLE_XDEBUG_WARN 1
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

ENV HOME /root

RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]

# Upgrade the container
RUN apt-get clean && \
    apt-get update && \
    apt-get upgrade -y

# Nginx-PHP Installation
RUN apt-get install -y nano unzip build-essential software-properties-common apt-utils curl wget
RUN add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository -y ppa:nginx/stable
RUN add-apt-repository -y ppa:maxmind/ppa
RUN add-apt-repository -y ppa:git-core/ppa
RUN apt-get update
RUN apt-get full-upgrade -y

# Install php
RUN apt-get install -y php7.3

# Install extension php
RUN apt-get install -y php7.3-cli php7.3-fpm php7.3-curl php7.3-gd php7.3-mbstring php7.3-zip php7.3-mysql php7.3-xml php7.3-json php7.3-intl php7.3-bcmath

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.3/cli/php.ini

RUN echo "opcache.memory_consumption = 256" \
         >> /etc/php/7.3/fpm/php.ini

RUN echo "opcache.memory_consumption = 256" \
         >> /etc/php/7.3/cli/php.ini

RUN echo "opcache.max_accelerated_files = 20000" \
         >> /etc/php/7.3/fpm/php.ini

RUN echo "opcache.max_accelerated_files = 20000" \
         >> /etc/php/7.3/cli/php.ini

RUN echo "opcache.validate_timestamps = 0" \
         >> /etc/php/7.3/fpm/php.ini

RUN echo "opcache.validate_timestamps = 0" \
         >> /etc/php/7.3/cli/php.ini

 RUN echo "realpath_cache_ttl = 600" \
         >> /etc/php/7.3/fpm/php.ini

RUN echo "realpath_cache_ttl = 600" \
         >> /etc/php/7.3/cli/php.ini



# Install nginx
RUN cd /tmp/ && wget http://nginx.org/keys/nginx_signing.key
RUN apt-key add /tmp/nginx_signing.key
RUN sh -c "echo 'deb http://nginx.org/packages/mainline/ubuntu/ '$(lsb_release -cs)' nginx' > /etc/apt/sources.list.d/Nginx.list"
RUN apt-get update
RUN apt-get install -y nginx
RUN nginx -v

# Install git
RUN apt-get install -y git

# Install memcached
RUN apt-get install -y php7.3-memcached memcached

# Cleanup
RUN apt-get remove --purge -y python-software-properties && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.3/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.3/fpm/php.ini

RUN mkdir /log
RUN mkdir -p     /var/www
ADD default   	 /etc/nginx/conf.d/default.conf
#ADD default   	 /etc/nginx/sites-available/default.conf
RUN mkdir        /etc/service/nginx
ADD nginx.sh  	 /etc/service/nginx/run
RUN chmod +x     /etc/service/nginx/run
RUN mkdir        /etc/service/phpfpm
ADD phpfpm.sh 	 /etc/service/phpfpm/run
RUN chmod +x     /etc/service/phpfpm/run
RUN mkdir        /etc/service/memcached
ADD memcached.sh /etc/service/memcached/run
RUN chmod +x     /etc/service/memcached/run
#RUN mkdir        /etc/nginx/sites-enabled
#RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

RUN service php7.3-fpm start

# Permission fix
RUN usermod -u 1000 www-data
RUN usermod -a -G www-data nginx

# Expose ports
EXPOSE 80
EXPOSE 443
# End Nginx-PHP

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add path the phpunit (project level)
ENV PATH /var/www/vendor/bin:$PATH

# Set working dir
WORKDIR /var/www
