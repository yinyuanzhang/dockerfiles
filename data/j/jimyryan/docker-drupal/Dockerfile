FROM alpine
MAINTAINER JimyRyan

# persistent / runtime deps
RUN set -e \
	&& apk add --update --no-cache --virtual .persistent-deps \ 
		bash \
		tzdata \
		ca-certificates \
		curl \
		letsencrypt \
		apk-cron

# Remove the apt list
RUN rm -rf /var/cache/apk/*

#Set timezone
RUN set -e \
	&& cp -f /usr/share/zoneinfo/Europe/Paris /etc/localtime \
	&& echo "Europe/Paris" > /etc/timezone
	
# ensure www-data user exists and /var/www/html exists
# 82 is the standard uid/gid for "www-data" in Alpine
# 33 is the standard uid/gid for www-data in debian
RUN set -e \	
	&& addgroup -g 82 -S www-data \
	&& adduser -u 82 -D -S -G www-data www-data	\
	&& mkdir -p /var/www/html

# Crontab
RUN set -e \
	&& mkdir -p /etc/periodic/1min \
	&& mkdir -p /etc/periodic/5min \
	&& mkdir -p /etc/periodic/10min \
	&& echo -e "*/1\t*\t*\t*\t*\trun-parts /etc/periodic/1min" >> /etc/crontabs/root \
	&& echo -e "*/5\t*\t*\t*\t*\trun-parts /etc/periodic/5min" >> /etc/crontabs/root \
	&& echo -e "*/10\t*\t*\t*\t*\trun-parts /etc/periodic/10min" >> /etc/crontabs/root
	
# Enable cron tab
ENV LETSENCRYPT_ENABLE_CRON_FOR_AUTO_RENEW true
VOLUME /var/log/cron

WORKDIR /var/www/html
VOLUME /var/www/html

# web server config
# Copy the config file for tmp (will be copy at the right place by the entrypoint script)
RUN mkdir -p /usr/local/etc/nginx/conf.d
COPY conf/nginx/*.conf /usr/local/etc/nginx/conf.d/

VOLUME /etc/nginx/conf.d	
	
# Waiter
# Version of dockerize (waiter)
ENV DOCKERIZE_VERSION 0.1.0
# Dockerize will wait 30 min
ENV DOCKERIZE_TIMEOUT 1800
# By default, don't wait any services
# For multiple service : php:9000,mysql:3306
ENV DOCKERIZE_WAIT_SERVICES=
# By default, will listen port 5000 when ready
ENV CONTAINER_TCP_SERVICES_READY_PORT 5000
ENV LETSENCRYPT_HTTPS_CERTS_OK_TCP_SERVICES_READY_PORT=5002

EXPOSE $CONTAINER_TCP_SERVICES_READY_PORT
EXPOSE $LETSENCRYPT_HTTPS_CERTS_OK_TCP_SERVICES_READY_PORT

RUN set -xe \
	&& curl -fSL "https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" -o /tmp/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \
	&& tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz

# Entrypoint & environement variable
COPY /*.sh /
COPY bin/waitsig /usr/bin/
RUN set -e \
	&& chmod 700 /*.sh \
	&& chmod 700 /usr/bin/waitsig

# https://www.drupal.org/node/3060/release
ENV DRUPAL_VERSION 8.0.6
ENV DRUPAL_MD5 952c14d46f0b02bcb29de5c3349c19ee	

ENV SITE_SECURE false
ENV SITE_NAME www.example.com
ENV NGINX_SERVER_NAME_MAIN_DOMAINS example.com www.example.com

# This is for the build in web server of letsencrypte
EXPOSE 80

ENV LETSENCRYPT_DEBUG false
ENV LETSENCRYPT_EMAIL contact@example.com
ENV LETSENCRYPT_DOMAINS_STRING_PARAM -d example.com -d www.example.com
ENV LETSENCRYPT_KEY_SIZE 4096

VOLUME /var/log/letsencrypt
VOLUME /etc/letsencrypt/live
VOLUME /etc/letsencrypt

# Possibility to call the Docker Cloud trigger API for reload in
ENV CALL_API_URL_TRIGGER_WHEN_READY=

ENTRYPOINT ["/my-entrypoint.sh"]

CMD ["waitsig"]