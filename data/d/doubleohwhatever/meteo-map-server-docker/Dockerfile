##
# idtstudios/meteo-map-server
#
# Ubuntu 16.04 Xenial Xerus
# FROM ubuntu:xenial
FROM geographica/gdal2:2.4.0

MAINTAINER idtstudios

ENV GIT_REPO https://github.com/user/repo.git
#ENV SERVER_POOL_ADDRESS_DEFAULT server.tld:port
ENV SERVER_FQDN server.domain.com
ENV SERVER_SSL_ENABLED no


# Load assets
WORKDIR /usr/local/

# Copy files
COPY crontab /etc/cron.d/update-cron
COPY entry.sh /usr/local/entry.sh
COPY wgrib2.sh /usr/local/wgrib2.sh
COPY wgrib2.tar.gz /usr/local/wgrib2.tar.gz

# Configure permissions
RUN chmod 0644 /etc/cron.d/update-cron
RUN chmod +x /usr/local/entry.sh
RUN chmod +x /usr/local/wgrib2.sh
RUN chmod 0755 /usr/local/wgrib2.tar.gz

#Install packages
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-get update -y && apt-get install -y --allow-unauthenticated \
    build-essential \
    checkinstall \
    gcc \
    apache2 \
    libapache2-mod-php7.2 \
    php \
    php-sqlite3 \
    php-gd \
    php-curl \
    php7.2-mysql \
    php7.2-xml \
    php7.2-dev \
    php7.2-mbstring \
    imagemagick \
    ffmpeg \
    unzip \
    libtiff5-dev \
    libpng-dev \
    zlib1g-dev \
    python-pip \
    python-setuptools \
    python-cffi \
    libtiff5 \
    libvips \
    python-qt4 \
    libvips-dev \
    optipng \
    pngquant \
    cron \
    software-properties-common \
    php-imagick \
    git \
    curl \
    gfortran \
    parallel \
    libmysqlclient-dev \
    wget

# Setup PHP Redis
RUN no '' | pecl install -f redis
RUN bash -c "echo extension=redis.so > /etc/php/7.2/apache2/conf.d/redis.ini"
RUN bash -c "echo extension=redis.so > /etc/php/7.2/cli/conf.d/redis.ini"


# Setup Apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf && \
 a2enconf servername && a2enmod rewrite

# Install gdal2mbtiles
RUN pip install --upgrade pip
RUN pip install Pillow
RUN pip install gdal2mbtiles

# Install gribdoctor (yes, I know we are installing, uninstalling then installing. Just roll with it)
RUN pip install gribdoctor --pre
RUN pip uninstall gribdoctor -y
RUN pip install git+git://github.com/idtstudios/grib-doctor

# Install wgrib2
RUN /usr/local/wgrib2.sh

# Setting up wgrib2 (Part 1)
#RUN cd /usr/local
#RUN curl -o wgrib2.tar.gz "ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz.v2.0.2"
#RUN tar zxf wgrib2.tar.gz
##RUN cd /usr/local/grib2
##RUN FC=gfortran
##RUN export FC
##RUN make
##RUN cp /usr/local/grib2/wgrib2/wgrib2 /usr/bin/wgrib2
#RUN cd /usr/local

# New php.ini
RUN rm -Rf /etc/php/7.0/apache2/php.ini
COPY php.ini /etc/php/7.0/apache2/php.ini
RUN rm -Rf /etc/php/7.1/apache2/php.ini
COPY php.ini /etc/php/7.1/apache2/php.ini
RUN rm -Rf /etc/php/7.2/apache2/php.ini
COPY php.ini /etc/php/7.2/apache2/php.ini
RUN rm -Rf /etc/php/7.3/apache2/php.ini
COPY php.ini /etc/php/7.3/apache2/php.ini


RUN rm -Rf /var/www
RUN mkdir /var/www
RUN chmod +0755 /var/www
RUN mkdir /var/data
RUN chmod +0755 /var/data
RUN mkdir /var/data/mapgen-basemap-tile-cache
RUN chmod +0777 /var/data/mapgen-basemap-tile-cache
RUN mkdir /var/data/mapgen-data-tile-cache
RUN chmod +0777 /var/data/mapgen-data-tile-cache

#Install let's encrypt
#RUN mkdir /var/www/letsencrypt
#RUN ln -s /var/www/letsencrypt /etc/letsencrypt
#RUN yes | add-apt-repository ppa:certbot/certbot
#RUN apt-get update -y && apt-get install -y python-certbot-apache

VOLUME /var/www
VOLUME /var/data
VOLUME /tmp
EXPOSE 80 443

# Run the command on container startup
ENTRYPOINT ["/usr/local/entry.sh"]
#CMD cron && tail -f /var/log/cron.log
