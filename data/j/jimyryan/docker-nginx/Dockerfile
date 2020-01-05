# Debian
FROM nginx:latest 
MAINTAINER JimyRyan

#################################################################################
#################################################################################
#                                                                               #
#                [START :: TIMEZONE, LOCALE & UPDATE / UPGRADE]                 #
#                                                                               #
#################################################################################
RUN set -xe \
	&& apt-get update -y \
    && apt-get install -y locales

# Set locale and timezone 
ENV LANGUAGE=fr_FR.UTF-8
ENV LANG=fr_FR.UTF-8
ENV LC_ALL=fr_FR.UTF-8
ENV TZ=Europe/Paris

# Change locale and timezone 
RUN set -xe \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && sed -i -e 's/# '$LANG' UTF-8/'$LANG' UTF-8/' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=$LANG \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Update distribution
RUN apt-get update -y \
    && apt-get upgrade -y
#################################################################################
#                                                                               #
#                   [END :: TIMEZONE, LOCALE & UPDATE / UPGRADE]                #
#                                                                               #
#################################################################################
#################################################################################

RUN apt-get install -y netcat 

# For debug
#RUN apt-get install -y vim net-tools
	
# Copy and set default nginx settings
RUN mkdir -p /usr/local/etc/nginx \
	&& mkdir -p /etc/nginx/private \
	&& mkdir -p /etc/nginx/custom
COPY conf/nginx/ /usr/local/etc/nginx/

# Delete the default config file
RUN rm -rf /etc/nginx/conf.d/default.conf

RUN set -xe \
	&& mkdir -p /etc/nginx/conf.d \
	&& mkdir -p /var/log/nginx
VOLUME /etc/nginx/conf.d
VOLUME /etc/nginx/private
VOLUME /etc/nginx/custom
VOLUME /var/log/nginx

# Waiter
ENV DOCKERIZE_VERSION 0.1.0
ENV DOCKERIZE_TIMEOUT 1800
ENV DOCKERIZE_WAIT_SERVICES=
RUN set -xe \
	&& apt-get install -y wget \
	&& wget "https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" -O /tmp/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \
	&& tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz

# Remove the apt list
RUN rm -rf /var/lib/apt/lists/* 
	
# Entrypoint & environement variable
COPY /*.sh /
RUN set -xe \
	&& chmod 700 /*.sh

# Possibility to call the Docker Cloud trigger API for reload in
ENV CALL_API_URL_TRIGGER_WHEN_READY=	
	
ENV NGINX_CLIENT_MAX_BODY_SIZE 100m
ENV NGINX_DHPARAM_KEY_SIZE 4096
ENV SITE_SECURE true

# Auto with read parameter on linked container
#ENV LETSENCRYPT_HOST_ADDR www.example.com
#ENV LETSENCRYPT_HOST_PORT 80

# When nginx config init mode is ready
ENV NGINX_INIT_MODE_TCP_SERVICES_READY_PORT=5001
EXPOSE $NGINX_INIT_MODE_TCP_SERVICES_READY_PORT
	
ENTRYPOINT ["/my-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]