FROM php:7.1-apache

# Enabled apache modules
RUN a2enmod rewrite expires

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpng-dev \
        libfreetype6-dev \
        libjpeg-dev \
        libzip-dev \
        libtidy-dev \
        default-mysql-client \
        git \
        zip \
        unzip \
        wget \
        less \
        vim \
        nano \
        ssh \
        sudo \
        python \
        python-requests \
        cron \
    && rm -rf /var/lib/apt/lists/*

# Start services
RUN update-rc.d cron defaults && service cron start

# Install the PHP extensions we need
# enable-gd-native-ttf removed - effectless as of php5.5 and removed since 7.2
# https://www.php.net/manual/en/image.installation.php
RUN set -ex \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir=/usr/ \
    && docker-php-ext-install gd mysqli opcache pdo_mysql tidy \
    && pecl install xdebug redis zip \
    && docker-php-ext-enable redis zip
    
# Install wp-cli to control Wordpress installations
RUN set -ex \
    && curl -# https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -o /tmp/wp-cli.phar \
    && chmod +x /tmp/wp-cli.phar \
    && mv /tmp/wp-cli.phar /usr/local/bin/wp

# Install composer for installing php dependencies
RUN set -ex \
    && curl -# https://getcomposer.org/installer | \
       php -- --install-dir=/usr/local/bin --filename=composer

# Set PHP settings
RUN { \
        echo 'date.timezone = "UTC"'; \
        echo 'sendmail_path = ""'; \
        echo 'log_errors = 1'; \
        echo 'error_reporting = E_ALL & ~E_NOTICE'; \
        echo 'error_log = "/dev/stderr"'; \
        echo 'xdebug.max_nesting_level = 1000'; \
        echo 'max_input_vars = 5000'; \
        echo 'post_max_size = 512M'; \
        echo 'upload_max_filesize = 512M'; \
        echo 'short_open_tag = 0'; \
    } | tee $PHP_INI_DIR/conf.d/retreat-guru.ini

# Install Blackfire profiler probe
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \
    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \
    && mv /tmp/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so \
    && printf "extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" > $PHP_INI_DIR/conf.d/blackfire.ini

# Setup SSL self-signed certificate and SSL
COPY etc/ssl/*.key /etc/ssl/private/
COPY etc/ssl/*.pem /etc/ssl/certs/
RUN a2enmod ssl && a2ensite default-ssl
EXPOSE 443

# Setup our own root certificate
COPY etc/ssl/retreatguruCA.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates

# Install acme.sh to support LetsEncrypt certificates
RUN curl https://get.acme.sh | sh

# Copy scripts
COPY bin/* /usr/local/bin/
COPY etc/.bashrc /root/
COPY etc/.vimrc /root/

# Set up default working directory
WORKDIR /var/www/html

# Add non root user
RUN useradd -m noroot -u 1000 -s /bin/bash -g www-data
RUN echo 'noroot ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
