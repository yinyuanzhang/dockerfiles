FROM nginx:1.9.9
MAINTAINER koudaiiii "cs006061@gmail.com"

RUN mkdir -p /var/www/nginx-default
RUN mkdir -p /etc/nginx/switch

COPY files/nginx-docker.conf /etc/nginx/conf.d/
COPY files/http_gzip_static.conf /etc/nginx/conf.d/
COPY files/nginx.conf /etc/nginx/
COPY files/favicon.ico /var/www/nginx-default/
COPY files/status.html /var/www/nginx-default/
COPY files/run.sh /run.sh

RUN rm -f /etc/nginx/conf.d/default.conf
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

CMD ["./run.sh"]
