FROM bitnami/nginx:1.14
ADD ./docker/nginx/vhosts /opt/bitnami/nginx/conf/vhosts
COPY ./docker/nginx/nginx.conf /opt/bitnami/nginx/conf/nginx.conf
ADD . /app/web
WORKDIR /app
