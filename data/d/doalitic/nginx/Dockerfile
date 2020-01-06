FROM nginx:stable

LABEL maintainer="Moss team <devops@moss.sh>"

ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget && apt-get clean && rm -r /var/lib/apt/lists/*
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p /etc/templates
ADD server.key.tpl /etc/templates/
ADD server.crt.tpl /etc/templates/
ADD htpasswd.tpl /etc/templates/
ADD nginx.conf.tpl /etc/templates/
EXPOSE 80 443

# The following environment variables are available:
#
# NGINX_WORKER_PROCESSES         number of worker processes(optional, default: 1)
# NGINX_WORKER_CONNECTIONS       maximum number of simultaneous connections that can be opened by a worker process. (optional, default: 1024)
# NGINX_PHPFPM_HOST              PHP-FPM network address
# NGINX_PHPFPM_PORT              PHP-FPM network port
# NGINX_GUNICORN_HOST            Gunicorn network address
# NGINX_GUNICORN_PORT            Gunicorn network port
# NGINX_PORT_HOST                port where nginx is listening on the host
# NGINX_SERVER_NAME              nginx vhost name
# NGINX_KEEPALIVE_TIMEOUT        nginx keepalive timeout value (optional, default: 60)
# NGINX_ROOT                     nginx root directory (optional, default: /var/www)
# NGINX_SERVE_STATIC_FILES       if present, nginx will serve static files (optional)
# NGINX_SSL_CERTIFICATE          nginx ssl certificate content (optional)
# NGINX_SSL_KEY      		 nginx ssl private key content (optional)
# NGINX_REDIRECT_HTTP_TO_HTTPS   if present, nginx will redirect http traffic to https (optional)
# NGINX_REDIRECT_WWW_TO_NON_WWW  if present, nginx will redirect non-www NGINX_SERVER_NAME to NGINX_SERVER_NAME
# NGINX_TRY_INDEX_HTML		 if present, nginx will serve /index.html when $uri doesn't exist
# NGINX_DISABLE_SENDFILE	 if present, the sendfile nginx optimization will be disabled
# NGINX_AUTH_BASIC_REALM         if present, nginx will use HTTP Basic Auth
# NGINX_AUTH_BASIC_HTPASSWD      if present, nginx will use this as the content of the user db

CMD [ "dockerize", \
    "-template", "/etc/container/templates/server.key.tpl:/etc/ssl/private/server.key", \
    "-template", "/etc/container/templates/server.crt.tpl:/etc/ssl/private/server.crt", \
    "-template", "/etc/container/templates/nginx.conf.tpl:/etc/nginx/nginx.conf", \
    "-template", "/etc/container/templates/htpasswd.tpl:/etc/nginx/htpasswd", \
    "nginx", "-g", "daemon off;" ]

