FROM ubuntu:xenial

# Configurable parameters for build:
ENV PHP_VERSION 7.2

# Do not touch below this line
ENV TERM=linux

# Base dependencies
RUN \
  apt-get update && \
  apt-get install -y software-properties-common git curl supervisor unzip

# Install nginx
RUN \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx

# Configure nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-available/default
RUN sed -i "s/\[PHP_VERSION\]/$PHP_VERSION/" /etc/nginx/sites-available/default

# Make nginx log to foreground
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# Install PHP
RUN \
  echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej-php.list && \
  echo "deb http://ppa.launchpad.net/ondrej/php-qa/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej-php-qa.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \
  apt-get update && \
  apt-get -y --no-install-recommends install \
    php$PHP_VERSION-fpm \
    php$PHP_VERSION-mysql \ 
    php$PHP_VERSION-curl \
    php$PHP_VERSION-gd \
    php$PHP_VERSION-xml \
    php$PHP_VERSION-mbstring \
    php$PHP_VERSION-imap \
    php$PHP_VERSION-zip \
    php$PHP_VERSION-xml

# Configure PHP
RUN sed -i 's/^;cgi.fix_pathinfo=.*$/cgi.fix_pathinfo=0/' /etc/php/$PHP_VERSION/fpm/php.ini
RUN sed -i 's/^memory_limit =.*$/memory_limit = 512M/' /etc/php/$PHP_VERSION/fpm/php.ini
RUN sed -i 's/^upload_max_filesize =.*$/upload_max_filesize = 128M/' /etc/php/$PHP_VERSION/fpm/php.ini
RUN sed -i 's/^post_max_size =.*$/post_max_size = 128M/' /etc/php/$PHP_VERSION/fpm/php.ini
RUN mkdir /var/run/php

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Supervisor configuration
COPY supervisor.conf /supervisor.conf
RUN sed -i "s/\[PHP_VERSION\]/$PHP_VERSION/" /supervisor.conf

# Add default webroot
COPY default_webroot /webroot

# Cleanup
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer
    
# Runtime command
CMD ["supervisord","-c","/supervisor.conf"]

EXPOSE 80
