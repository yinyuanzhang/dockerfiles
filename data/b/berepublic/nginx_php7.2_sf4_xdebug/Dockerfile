FROM berepublic/ubuntu-baseimage-docker

MAINTAINER BeRepublic

ENV DEBIAN_FRONTEND noninteractive
ENV COMPOSER_DISABLE_XDEBUG_WARN 1

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
RUN apt-get install -y nano unzip build-essential python-software-properties
RUN add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update

# Install php
RUN apt-get install -y php7.2 php7.2-common php7.2-cli php7.2-fpm

# Install extension php
RUN apt-get install -y php7.2-mysql php7.2-curl php7.2-gd php7.2-intl php7.2-json php7.2-xml php7.2-zip php7.2-mbstring php7.2-bcmath

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/cli/php.ini

# Install nginx
RUN apt-get install -y nginx

# Install git
RUN apt-get install -y git

# Install xdebug
RUN apt-get install -y php7.2-xdebug

# Install memcached
RUN apt-get install -y php7.2-memcached memcached

# Cleanup
RUN apt-get remove --purge -y python-software-properties && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.2/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.2/fpm/php.ini

RUN mkdir /log
RUN mkdir -p     /var/www
ADD default   	 /etc/nginx/sites-available/default
RUN mkdir        /etc/service/nginx
ADD nginx.sh  	 /etc/service/nginx/run
RUN chmod +x     /etc/service/nginx/run
RUN mkdir        /etc/service/phpfpm
ADD phpfpm.sh 	 /etc/service/phpfpm/run
RUN chmod +x     /etc/service/phpfpm/run
RUN mkdir        /etc/service/memcached
ADD memcached.sh /etc/service/memcached/run
RUN chmod +x     /etc/service/memcached/run

RUN service php7.2-fpm start

# Permission fix
RUN usermod -u 1000 www-data

# Expose ports
EXPOSE 80
EXPOSE 443
# End Nginx-PHP

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add path the phpunit (project level)
ENV PATH /var/www/vendor/bin:$PATH

# Set working dir
WORKDIR /var/www
