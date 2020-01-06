FROM phppm/nginx:1.0.1-2 as ppmbase

FROM composer/composer:1.1 as composer

ARG version=1.0.1
ARG http_version=dev-master
RUN mkdir /ppm && cd /ppm && composer require php-pm/php-pm:${version} && composer require wanghanlin/php-pm-httpkernel-adapter:${http_version}

FROM alpine:3.7

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    echo "UTC" | tee /etc/timezone && \
    apk del tzdata

RUN apk --no-cache add \
    php7 php7-opcache php7-fpm php7-cgi php7-ctype php7-json php7-dom php7-zip php7-zip php7-gd \
    php7-curl php7-mbstring php7-redis php7-mcrypt php7-posix php7-pdo_mysql php7-tokenizer php7-simplexml php7-session \
    php7-xml php7-sockets php7-openssl php7-fileinfo php7-ldap php7-exif php7-pcntl php7-xmlwriter php7-phar php7-zlib \
    php7-intl php7-gmp
    
COPY --from=ppmbase /etc/php7/php.ini /etc/php7/php.ini
RUN echo "upload_max_filesize = 32M" >> /etc/php7/php.ini

RUN apk --no-cache add bash curl git openssh-client nodejs nodejs-npm supervisor jpegoptim optipng pngquant gifsicle libpng-dev

RUN apk --no-cache add nginx

COPY --from=ppmbase /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default
COPY --from=ppmbase /etc/nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

COPY --from=composer /ppm /ppm

WORKDIR /var/www

RUN mkdir -p /root/.ssh && \
    ssh-keyscan -H gitlab.com >> /root/.ssh/known_hosts 
    
RUN npm install -g yarn && npm install -g svgo

RUN apk add --no-cache \
	xvfb ttf-freefont fontconfig dbus \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.0 libssl1.0 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family \

    && \

    apk add --no-cache wkhtmltopdf --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \

    && \

    mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf-origin && \
    echo $'#!/usr/bin/env sh\n\
Xvfb :0 -screen 0 1024x768x24 -ac +extension GLX +render -noreset & \n\
DISPLAY=:0.0 wkhtmltopdf-origin $@ \n\
killall Xvfb\
' > /usr/bin/wkhtmltopdf && \
    chmod +x /usr/bin/wkhtmltopdf

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

COPY --from=ppmbase /etc/app/run.sh /etc/app/run.sh

ENTRYPOINT ["/bin/bash", "/etc/app/run.sh"]

