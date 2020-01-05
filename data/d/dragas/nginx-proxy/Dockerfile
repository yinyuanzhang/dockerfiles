FROM jwilder/nginx-proxy:alpine
LABEL maintainer="stefano@dragas.it"
RUN { \
      echo 'client_max_body_size 0;'; \
    } > /etc/nginx/conf.d/unrestricted_client_body_size.conf

RUN { \
      	echo 'gzip on; \
	gzip_static  on; \
            gzip_disable "msie6"; \
	      gzip_vary on; \
	      gzip_proxied any; \
	      gzip_comp_level 6; \
	      gzip_buffers 16 8k; \
	      gzip_http_version 1.1; \
	      gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;'; \
    } > /etc/nginx/conf.d/gzip_enabled.conf
 
