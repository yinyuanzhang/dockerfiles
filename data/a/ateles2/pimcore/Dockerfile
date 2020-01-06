FROM phusion/baseimage:0.11
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8 TERM=linux LANG=C

COPY ./phusion/install-composer-debian.sh /tmp/install-composer.sh
COPY ./phusion/install-pimcore-extra.sh /install-pimcore-extra.sh
COPY ./phusion/modify-php-ini.sh /modify-php-ini.sh
COPY phusion/start-apache.sh /usr/local/bin/start-apache.sh

RUN add-apt-repository ppa:ondrej/php >/dev/null\
    && apt-get update >/dev/null \
    && DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends \
    wget \
    unzip \
    iputils-ping \
    apache2 \
    php7.1 \
    php7.1-cli \
    php7.1-curl \
    php7.1-xml \
    php7.1-xsl \
    php7.1-soap \
    php7.1-gd \
    php7.1-mcrypt \
    php7.1-zip \
    php7.1-mbstring \
    php7.1-bcmath \
    php7.1-json \
    php7.1-intl \
    php7.1-mysql \
    php7.1-readline \
    php-redis \
    php-xdebug \
    php-imagick \
    php7.1-bz2 \
    libapache2-mod-php7.1 \
    php7.1-mbstring \
    php7.1-imagick \
    php7.1-curl \
    php7.1-redis \
    php7.1-apcu \
    xz-utils \
    poppler-utils \
    libpng16-16 \
    libimage-exiftool-perl \
    html2text \
    locales \
    ncurses-term \
    rsync \
    ffmpeg \
    lftp \
    nano \
    net-tools \
    && chmod +x /tmp/install-composer.sh && sync && /tmp/install-composer.sh \
    && mv /composer.phar /usr/local/bin/composer \
    && chmod +x /install-pimcore-extra.sh && sync &&  /install-pimcore-extra.sh && rm /install-pimcore-extra.sh \
    && chmod +x /modify-php-ini.sh && sync &&  /modify-php-ini.sh && rm /modify-php-ini.sh \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen en_US.UTF-8 \
    && mkdir -p /var/www/html \
    && a2enmod remoteip && a2enmod info && a2enmod rewrite \
    && apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get autoremove -y \
    && rm -r /tmp/* && rm /etc/apache2/sites-enabled/* \
    && ln -fs /usr/share/zoneinfo/Europe/Stockholm /etc/localtime \
    && echo "Europe/Stockholm" > /etc/timezone

WORKDIR /var/www/html
EXPOSE 80
# Start Apache
CMD /usr/local/bin/start-apache.sh
