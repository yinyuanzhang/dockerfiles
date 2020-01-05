FROM php:7.1.12-apache

RUN apt-get update && apt-get install -y lsb-release \
    && echo "deb http://deb.debian.org/debian $(lsb_release -sc)-backports main" > /etc/apt/sources.list.d/backports.list \
    && apt-get update && apt-get install -y --no-install-recommends \
      autoconf automake libtool nasm make pkg-config libz-dev build-essential g++ \
      zlib1g-dev libicu-dev libbz2-dev libjpeg-dev libpng-dev libfreetype6-dev libc-client-dev \
      libkrb5-dev libxml2-dev libxslt1.1 libxslt1-dev locales locales-all \
      ffmpeg html2text ghostscript libreoffice pngcrush jpegoptim exiftool poppler-utils git wget \
      libx11-dev libmcrypt-dev\
    && wget http://www.imagemagick.org/download/ImageMagick.tar.gz \
      && tar -xvf ImageMagick.tar.gz \
      && cd ImageMagick-7.* \
      && ./configure \
      && make \
      && make install \
      && ldconfig /usr/local/lib \
      && cd .. \
      && rm -rf ImageMagick* \
    && a2enmod rewrite headers \
    && docker-php-ext-install intl mbstring mcrypt mysqli bcmath bz2 gd soap xmlrpc xsl pdo pdo_mysql fileinfo exif zip opcache \
    && docker-php-ext-enable intl mbstring mcrypt mysqli bcmath bz2 gd soap xmlrpc xsl pdo pdo_mysql fileinfo exif zip opcache\
    && pecl install xdebug redis imagick \
    && docker-php-ext-enable xdebug redis imagick \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install imap \
    && docker-php-ext-enable imap \
    \
    && cd ~ \
    \
    && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
      && tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
      && mv wkhtmltox/bin/wkhtmlto* /usr/bin/ \
      && rm -rf wkhtmltox \
    \
    && git clone https://github.com/mozilla/mozjpeg.git  \
      && cd mozjpeg \
      && autoreconf -fiv \
      && ./configure \
      && make \
      && make install \
      && ln -s /opt/mozjpeg/bin/cjpeg /usr/bin/cjpeg \
      && cd .. \
      && rm -rf mozjpeg \
    && git clone https://github.com/google/zopfli.git \
      && cd zopfli \
      && make \
      && cp zopfli /usr/bin/zopflipng \
      && cd .. \
      && rm -rf zopfli \
    && wget http://static.jonof.id.au/dl/kenutils/pngout-20150319-linux.tar.gz \
      && tar -xf pngout-20150319-linux.tar.gz \
      && rm pngout-20150319-linux.tar.gz \
      && cp pngout-20150319-linux/x86_64/pngout /bin/pngout \
      && cd .. \
      && rm -rf pngout-20150319-linux \
    && wget http://prdownloads.sourceforge.net/advancemame/advancecomp-1.17.tar.gz \
      && tar zxvf advancecomp-1.17.tar.gz \
      && cd advancecomp-1.17 \
      && ./configure \
      && make \
      && make install \
      && cd .. \
      && rm -rf advancecomp-1.17 \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && apt-get autoremove -y \ 
      && apt-get remove -y autoconf automake libtool nasm make pkg-config libz-dev build-essential g++ \
      && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer

RUN usermod -u 1000 www-data
RUN usermod -G staff www-data

ENV APACHE_DOCUMENT_ROOT /var/www/html/web
ENV PHP_DEBUG 0

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

CMD ["apache2-foreground"]
