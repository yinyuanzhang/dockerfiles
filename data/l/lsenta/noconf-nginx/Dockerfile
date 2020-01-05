FROM nginx:1.9
MAINTAINER Kyle Mathews "mathews.kyle@gmail.com" # https://github.com/KyleAMathews/docker-nginx
MAINTAINER Laurent Senta "laurent.senta@gmail.com" # This fork

RUN rm /etc/nginx/nginx.conf /etc/nginx/mime.types
RUN mkdir /etc/nginx/ssl /etc/nginx/sites-available /etc/nginx/sites-enabled

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/basic.conf /etc/nginx/basic.conf
COPY nginx/mime.types /etc/nginx/mime.types
COPY nginx/directive-only /etc/nginx/directive-only
COPY nginx/location /etc/nginx/location

COPY entry.sh /etc/nginx/
COPY sites-available /etc/nginx/sites-available

EXPOSE 80

# This is the var you can override to mount volumes from.
ENV STATIC_FOLDER=/var/www

WORKDIR "/etc/nginx"
CMD ["./entry.sh"]

