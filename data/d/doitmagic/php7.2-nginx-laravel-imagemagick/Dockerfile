FROM phusion/baseimage:latest

LABEL maintainer "Doitmagic <razvan@doitmagic.com>"

# add NGINX official stable repository
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/nginx.list && \
# add PHP7 unofficial repository (https://launchpad.net/~ondrej/+archive/ubuntu/php)
echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/php.list && \
# install packages
apt-get update && \
    apt-get -y --force-yes --no-install-recommends install  \
    supervisor \
    curl \
    nginx \
    zip \
    unzip \
    php7.2-fpm php7.2-dev php7.2-cli php7.2-common php7.2-curl php7.2-gd php7.2-intl php7.2-json php7.2-mbstring  php7.2-mysql php7.2-opcache  php7.2-soap  php7.2-xml php7.2-xmlrpc php7.2-xsl php7.2-zip php7.2-gd \
    git wget openssl libssl-dev zlib1g-dev libicu-dev g++ make cmake libuv-dev libgmp-dev uuid-dev libpcre3-dev php-pear  libmagickwand-dev imagemagick ghostscript --allow-unauthenticated
RUN apt-get install -yq \
        libfreetype6-dev \
        libmcrypt-dev \
        libpng12-dev \
        libjpeg-dev \
        libpng-dev --allow-unauthenticated   
# clear apt cache and remove unnecessary packages
RUN mkdir -p /etc/nginx/htpasswd/  \
 mkdir -p /etc/nginx/ssl && \ 
 # php7.2-fpm will not start if this directory does not exist
mkdir /run/php && \
echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null && \
# Install the composer
curl -sS http://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer  && \
chmod +x /usr/bin/composer  && \
# configure NGINX as non-daemon
echo "daemon off;" >> /etc/nginx/nginx.conf  

COPY config/php/php.ini /etc/php/7.2/fpm/php.ini 
# configure php-fpm as non-daemon
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.2/fpm/php-fpm.conf   && \
# clear apt cache and remove unnecessary packages
apt-get autoclean && apt-get -y autoremove && \
# backup default default config for NGINX
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak && \
apt-get autoclean -y --force-yes && \
apt-get clean -y --force-yes


# installs wkhtmltopdf
RUN apt-get install -y --allow-unauthenticated wkhtmltopdf && \
    ln -s /usr/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf 


# installs unoconv
RUN apt-get install -y unoconv --allow-unauthenticated && \
    ln -s /usr/bin/unoconv /usr/local/bin/unoconv 
COPY config/unoconv.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/unoconv.sh

    # Install imagick extension
RUN pecl install imagick 

RUN   echo extension=imagick.so > /etc/php/7.2/mods-available/imagick.ini \
    && phpenmod imagick  && service php7.2-fpm restart

# copy config file for Supervisor
COPY config/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/nginx/default /etc/nginx/sites-enabled/default

RUN usermod -u 1000 www-data

# NGINX mountable directory for apps, mountable directories for config and logs
VOLUME ["/var/www","/etc/nginx/sites-available", "/etc/nginx/ssl", "/var/log/nginx"]

WORKDIR /var/www

# NGINX ports
EXPOSE 80 443

CMD ["/usr/bin/supervisord"]
