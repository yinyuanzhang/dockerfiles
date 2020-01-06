FROM jwilder/nginx-proxy
MAINTAINER Christoph Auer <auer.chrisi@gmx.net>

RUN { \
      echo 'server_tokens off;'; \
      echo 'client_max_body_size 100m;'; \
    } > /etc/nginx/conf.d/my_proxy.conf
