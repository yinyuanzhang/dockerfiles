FROM php:7-apache

ENV KUSERFEEDBACK_VERSION=21681a1e2e2e8571fe045d3ebd12cb1d0877a96e

RUN a2enmod rewrite authnz_ldap
RUN apt-get update \
	&& apt-get -y install libmariadbclient-dev git \
	&& rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-install -j$(nproc) pdo_mysql
COPY php.ini /usr/local/etc/php/

RUN git clone https://github.com/KDE/kuserfeedback.git /kuserfeedback \
	&& cd /kuserfeedback \
	&& git checkout ${KUSERFEEDBACK_VERSION} \
	&& cp -a src/server/. /var/www/html \
	&& cd / \
	&& rm -rf /kuserfeedback
ADD config /var/www/html/config

ADD htaccess-ldap /
RUN cat /htaccess-ldap >> /var/www/html/analytics/.htaccess \
	&& cat /htaccess-ldap >> /var/www/html/admin/.htaccess

ADD apache-envvars /
RUN cat /apache-envvars >> /etc/apache2/envvars
