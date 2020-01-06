FROM ubuntu:18.04

LABEL maintainer="Lucas van Staden lucas.vanstaden@enjo.com.au"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install software-properties-common tzdata

RUN apt-get update

RUN apt-get install -y --no-install-recommends \
	build-essential \
	software-properties-common \
	cron \
	nano \
	git \
	curl \
	supervisor \
    php-fpm \
    php-cli \
    php-mysql \
    php-curl \
    php-gd \
    php-redis \
    php-xml \
    php-soap \
    php-mbstring \
    php-zip \
	nginx \
	ssh \
	npm \
	joe \
	unzip \
	php-curl \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD nginx/default   /etc/nginx/sites-available/default
ADD nginx/.htpasswd   /etc/nginx/

# Install nodejs
RUN npm install express serve-static

# Install ssh key
RUN mkdir -p /root/.ssh/ && touch /root/.ssh/known_hosts

# Install Composer
# Install prestissimo
# Install Satis and Satisfy
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
	&& /usr/local/bin/composer global require hirak/prestissimo
RUN git clone https://github.com/ProxiBlue/satisfy.git /satisfy && cd /satisfy && composer install
RUN mkdir /satisfy/vendor/composer -p && chown www-data:www-data /satisfy -R && chmod -R 777 /satisfy && rm -rf /root/.composer/cache/*
ADD scripts /app/scripts

ADD scripts/crontab /etc/cron.d/satis-cron
ADD satis.json /root/satis.json
ADD server.js /app/server.js
RUN chmod 0644 /etc/cron.d/satis-cron \
	&& touch /var/log/satis-cron.log \
	&& chmod 777 /app/server.js \
	&& chmod +x /app/scripts/startup.sh

ADD supervisor/0-install.conf /etc/supervisor/conf.d/0-install.conf
ADD supervisor/1-cron.conf /etc/supervisor/conf.d/1-cron.conf
ADD supervisor/2-nginx.conf /etc/supervisor/conf.d/2-nginx.conf
ADD supervisor/3-php.conf /etc/supervisor/conf.d/3-php.conf
ADD supervisor/4-node.conf /etc/supervisor/conf.d/4-node.conf

RUN sed -i '/^;catch_workers_output/ccatch_workers_output = yes' "/etc/php/7.2/fpm/pool.d/www.conf"

RUN mkdir /satisfy/app/../var/cache/dev -p && chmod 777 /satisfy/app/../var -R

WORKDIR /app

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]

EXPOSE 80
EXPOSE 443

