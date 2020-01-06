# Source of this Dockerfile taken from https://github.com/docker-library/drupal/blob/597c24e51daca68815cc687d8cc147d089db103a/7/apache/Dockerfile
#
# from https://www.drupal.org/requirements/php#drupalversions
FROM php:5.6.40-apache

# install the PHP extensions we need
RUN set -ex; \
	\
	if command -v a2enmod; then \
		a2enmod rewrite; \
	fi; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libjpeg-dev \
		libpng-dev \
		libpq-dev \
	; \
	\
	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
	docker-php-ext-install -j "$(nproc)" \
		gd \
		opcache \
		pdo_mysql \
		pdo_pgsql \
		zip \
	; \
	\
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
	apt-mark auto '.*' > /dev/null; \
	apt-mark manual $savedAptMark; \
	ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
		| awk '/=>/ { print $3 }' \
		| sort -u \
		| xargs -r dpkg-query -S \
		| cut -d: -f1 \
		| sort -u \
		| xargs -rt apt-mark manual; \
	\
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

WORKDIR /var/www/html

RUN apt-get update; \
    apt-get install -y wget;

RUN \
    sed -i 's%/var/www/html%/opt/atlassian/pipelines/agent/build/public_html%' /etc/apache2/sites-available/000-default.conf; \
    sed -i 's%/var/www/html%/opt/atlassian/pipelines/agent/build/public_html%' /etc/apache2/sites-available/default-ssl.conf;

RUN { \
        echo '        ErrorLog /opt/atlassian/pipelines/agent/build/error.log'; \
        echo '        CustomLog /opt/atlassian/pipelines/agent/build/access.log combined'; \
        echo '        DirectoryIndex index.html index.htm index.php index.php4 index.php5'; \
		echo '        <Directory /opt/atlassian/pipelines/agent/build/public_html/>'; \
		echo '          Options -Indexes +IncludesNOEXEC +SymLinksIfOwnerMatch'; \
		echo '          allow from all'; \
		echo '          AllowOverride All Options=ExecCGI,Includes,IncludesNOEXEC,Indexes,MultiViews,SymLinksIfOwnerMatch'; \
		echo '          Require all granted'; \
		echo '        </Directory>'; \
	} > /tmp/apache.conf

RUN \
    sed -i '/DocumentRoot/r /tmp/apache.conf' /etc/apache2/sites-available/000-default.conf; \
    sed -i '/DocumentRoot/r /tmp/apache.conf' /etc/apache2/sites-available/default-ssl.conf;

RUN \
    mkdir -p /opt/atlassian/pipelines/agent/build/public_html; \
    chown -R www-data:www-data /opt/atlassian/pipelines/agent/build/public_html;

# Install mysql.
RUN export DEBIAN_FRONTEND="noninteractive"; apt-get -y install mysql-server
#RUN debconf-set-selections <<< "mysql-server mysql-server/root_password password root $1"
#RUN debconf-set-selections <<< "mysql-server mysql-server/root_password_again password root $1"

# Install lftp.
RUN apt-get update && \
   apt-get install -y lftp

# Install composer.
RUN apt-get update; \
    apt-get install -y git; \
    php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"; \
    EXPECTED_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig); \
    ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', '/tmp/composer-setup.php');"); \
    if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ] ; \
    then \
        echo 'ERROR: Invalid installer signature'; \
    else \
        php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer; \
    fi ;\
    rm /tmp/composer-setup.php;

# Install drush.
RUN php -r "readfile('https://github.com/drush-ops/drush/releases/download/8.1.18/drush.phar');" > drush
RUN chmod +x drush; \
    mv drush /usr/local/bin;

# Install drush-patch
RUN mkdir -p /root/.drush; \
cd /root/.drush; \
git clone https://bitbucket.org/sasa_jovanovic_esenca/drush-patchfile.git

# Install ssmtp.
RUN apt-get update && \
   apt-get install -y ssmtp && \
   apt-get clean

# SSMTP settings
COPY ssmtp.conf /etc/ssmtp/ssmtp.conf
# PHP mail settings
RUN echo 'sendmail_path = "/usr/sbin/ssmtp -t -i"' > /usr/local/etc/php/conf.d/mail.ini

