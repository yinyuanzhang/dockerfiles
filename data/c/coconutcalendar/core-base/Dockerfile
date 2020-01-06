FROM ubuntu:18.04

ENV PHPVERSION=7.4
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
		locales \
		software-properties-common \
		cron \
		curl \
		gpg-agent \
		zip \
		unzip \
		supervisor \

    # Generate locales
    && locale-gen en_CA.UTF-8 \
    && locale-gen fr_CA.UTF-8 \
    && locale-gen es_US.UTF-8 \

	# Add PHP and NGINX repositories
    && add-apt-repository -y ppa:ondrej/php \
    && add-apt-repository -y ppa:nginx/development \
    && apt-get update \

    # PHP
    && apt-get install -y --no-install-recommends \
		php-apcu \
		php-redis \
        php${PHPVERSION}-fpm \
        php${PHPVERSION}-cli \
        php${PHPVERSION}-curl \
        php${PHPVERSION}-gd \
        php${PHPVERSION}-intl \
        php${PHPVERSION}-mbstring \
        php${PHPVERSION}-mysql \
        php${PHPVERSION}-readline \
        php${PHPVERSION}-soap \
        php${PHPVERSION}-xml \
        php${PHPVERSION}-zip \
    && update-alternatives --set php /usr/bin/php${PHPVERSION} \
    && mkdir /run/php \

    # New Relic agent
    && curl -s https://download.newrelic.com/548C16BF.gpg | apt-key add - \
    && apt-add-repository "deb http://apt.newrelic.com/debian/ newrelic non-free" \
    && apt-get update \
    && apt-get install -y --no-install-recommends newrelic-php5 \
    && echo "newrelic.enabled = false" > /etc/php/${PHPVERSION}/mods-available/newrelic.ini \

	# NGINX
	&& apt-get install -y --no-install-recommends nginx \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \

    # Delete unnecessary packages and files
    && apt-get purge -y gpg-agent software-properties-common \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG en_CA.UTF-8
ENV LANGUAGE en_CA:en
ENV LC_ALL en_CA.UTF-8

COPY php-fpm.conf /etc/php/${PHPVERSION}/fpm/php-fpm.conf
COPY php-fpm.ini /etc/php/${PHPVERSION}/fpm/php.ini
COPY www.conf /etc/php/${PHPVERSION}/fpm/pool.d/www.conf
COPY php-cli.ini /etc/php/${PHPVERSION}/cli/php.ini
COPY default /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

EXPOSE 80

CMD ["/usr/local/bin/entrypoint.sh"]
