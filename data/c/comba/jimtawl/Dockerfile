FROM php:7.0-apache
MAINTAINER Michael Liebler <michael-liebler@janguo.de> (@mliebler)

# Disable remote database security requirements.
ENV JOOMLA_INSTALLATION_DISABLE_LOCALHOST_CHECK=1

# Enable Apache Rewrite Module
RUN a2enmod rewrite

# Install PHP extensions
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libmcrypt-dev zip unzip mysql-client git && rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install mcrypt
RUN docker-php-ext-install zip

VOLUME /var/www/html

# Define Joomla version and expected SHA1 signature
ENV JOOMLA_VERSION 3.8.0
ENV JOOMLA_SHA1 e15cfee1b31fe65b1c5038d605478404be9f64e2

# Download package and extract to web volume
RUN curl -o joomla.zip -SL https://github.com/joomla/joomla-cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-Full_Package.zip \
	&& echo "$JOOMLA_SHA1 *joomla.zip" | sha1sum -c - \
	&& mkdir /usr/src/joomla \
	&& unzip joomla.zip -d /usr/src/joomla \
	&& rm joomla.zip \
	&& cd /usr/src/joomla && sed -r 's/^(Options -Indexes.*)$/#\1/' htaccess.txt > .htaccess \
	&& chown -R www-data:www-data /usr/src/joomla


RUN cd /usr/src \
	&& git clone https://gitlab.janguo.de/radio-z/jimtawl.git \
	&& cd jimtawl \
    && JIMTAWLVERSION=$(cat version) \
    && sed "s/##version##/${JIMTAWLVERSION}/g" build_2/jimtawl.xml >  com_jimtawl/admin/jimtawl.xml \
    && sed "s/##version##/${JIMTAWLVERSION}/g" com_jimtawl/admin/jimtawl.xml >  com_jimtawl/jimtawl.xml \
    && sed "s/##version##/${JIMTAWLVERSION}/g" build_2/pkg_jimtawl.xml >  pkg_jimtawl.xml \
    && mkdir packages && zip -r packages/com_jimtawl.zip com_jimtawl \
    && zip -r packages/mod_jimtawlonair.zip modules/mod_jimtawlonair \
    && zip -r packages/mod_jimtawl_podcast.zip modules/mod_jimtawl_podcast \
    && zip -r packages/lib_comba.zip libraries/comba \
    && zip -r packages/jimtawl_search.zip plugins/jimtawl_search \
    && zip -r jimtawl-${JIMTAWLVERSION}.zip packages/* pkg_jimtawl.xml \
    && rm -Rf tests && rm -Rf build_2 && rm -Rf help && rm -f *.png && rm -f *.xcf && rm -f *.xml && rm -f *.package.php

ADD sql/sample_jimtawl.sql /usr/src/jimtawl/sample_jimtawl.sql.dist
ADD sql/sample_programme.sql /usr/src/jimtawl/sample_programme.sql.dist
ADD cli/addUser.php /usr/src/jimtawl/addUser.php
ADD cli/genSecret.php /usr/src/jimtawl/genSecret.php

# Copy init scripts and custom .htaccess

ENV JOOMLA_SITENAME "Jimtawl Calendar"
ENV JOOMLA_DB_HOST ""
ENV JOOMLA_DB_USER='root'
ENV JOOMLA_DB_PASSWORD='secret'
ENV JOOMLA_DB_NAME='joomla_db'
ENV JOOMLA_DB_PREFIX='jtwl'

ENV JOOMLA_ADMIN_EMAIL='admin@nowhere.tld'
ENV JOOMLA_ADMIN_USERNAME='jimtawladmin'
ENV JOOMLA_ADMIN_PASSWORD='secret'

COPY entrypoint.sh /entrypoint.sh
COPY makedb.php /makedb.php
ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
