FROM debian:9

WORKDIR /var/www/html

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Install pre-requisites
RUN apt-get update > /dev/null \
    && apt-get install --assume-yes \
        apache2 \
        cron \
        wget \
        curl \
        git \
        zip \
        unzip \
        gnupg \
        cron  \
        vim \
        apt-transport-https\
        > /dev/null

# Install PHP
RUN curl https://packages.sury.org/php/apt.gpg | apt-key add - \
    && echo "deb https://packages.sury.org/php/ stretch main" \
    | tee /etc/apt/sources.list.d/php5.list \
        && apt-get update > /dev/null \
        && apt-get install --assume-yes \
    php7.0 > /dev/null

# Install PHP modules
RUN apt install --assume-yes \
        php7.0-zip \
        php7.0-xml \
        php7.0-mcrypt \
        php7.0-imap \
        php7.0-mailparse \
        php7.0-opcache \
        php7.0-curl \
        php7.0-apcu \
        php7.0-pdo-mysql \
        php7.0-gd > /dev/null

 # Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=compose

# Install Mautic
RUN wget https://github.com/mautic/mautic/releases/download/2.15.2/2.15.2.zip \
    && unzip 2.15.2.zip -d ./

# Install Whitelabeler
RUN git clone https://github.com/nickian/mautic-whitelabeler.git whitelabeler

# Import cron
COPY mautic.crontab /var/www/html
RUN cat mautic.crontab | crontab -

# Seting permissions apache
RUN rm -f index.html \
    && chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html 

# Enable module apache
RUN a2enmod rewrite

# Config apache
COPY 000-default.conf /etc/apache2/sites-enabled/
RUN htpasswd -bc whitelabeler/.htpasswd mautic mautic@123

# Start cron
RUN service cron start 

CMD service cron restart  && apache2ctl -D FOREGROUND