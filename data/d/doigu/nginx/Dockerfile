# https://hub.docker.com/_/ubuntu/
FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
            ca-certificates \
            nginx \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
    && mv /etc/nginx/sites-available/default /etc/nginx/conf.d/default.conf \
    && rm -rf /etc/nginx/sites-available /etc/nginx/sites-enable
    
COPY nginx.conf /etc/nginx/
    
EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]