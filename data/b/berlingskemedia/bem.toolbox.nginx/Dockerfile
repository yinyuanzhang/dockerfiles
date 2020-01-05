#
# Nginx Dockerfile
#
# https://github.com/dockerfile/nginx
#

# Pull base image.
FROM ubuntu:18.10

ENV DOCKER_PORT 8080
ENV DATABASE_ENDPOINT rds_endpoint
ENV PHP_ELASTICACHE_ENDPOINT elasticache_endpoint
ENV ENVIRONMENT_NAME testing

# Secrets are made of php_environment/php_secret_rds
ENV PHP_SECRET_RDS bem.toolbox.code/rds

# Install necessary components (several layers)
RUN apt-get update && apt-get -y install software-properties-common awscli jq && \
#  add-apt-repository -y ppa:nginx/stable && \
   apt-get  install -y nginx php7.2-fpm curl && \
   echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
   chown -R www-data:www-data /var/lib/nginx && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy sites-config
ADD sites-available/*.conf /etc/nginx/sites-available/

# link toolbox.conf
RUN rm /etc/nginx/sites-enabled/* \
    && ln -sf /etc/nginx/sites-available/toolbox.conf /etc/nginx/sites-enabled/toolbox.conf 

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# add start file
ADD start_nginx.sh /usr/bin/start_nginx.sh

USER root
RUN chmod 700 /usr/bin/start_nginx.sh

# Define working directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["/usr/bin/start_nginx.sh"]

# Expose ports. But not on priviledged ports. 
EXPOSE $DOCKER_PORT
