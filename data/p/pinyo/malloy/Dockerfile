
FROM debian:sid-slim

MAINTAINER Laszlo Tosoki <tosoki.laszlo@fotex.net>

RUN apt-get update && apt-get upgrade -y &&			\
    apt-get install --no-install-recommends nginx -y &&		\
    apt-get clean

COPY default.index.html /var/www/html/index.html
COPY default /etc/nginx/sites-available/default

EXPOSE 8880
CMD ["nginx", "-g", "daemon off;"]
