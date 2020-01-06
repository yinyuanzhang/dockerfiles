FROM ubuntu:16.04
MAINTAINER Poshtiban.io


WORKDIR /app

COPY . /app

RUN sed -i "s|'http://127.0.0.1'|'https://atoms.poshtiban.com'|" src/app/services/endpoint.service.js

RUN chmod +x ./setup_6.x 
RUN ./setup_6.x

RUN apt-get update && apt-get install -y \
    nginx \
    nodejs \
    build-essential \
    libssl-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && echo "daemon off;" >> /etc/nginx/nginx.conf 



COPY ./docker/nginx-default /etc/nginx/sites-enabled/default

RUN npm -g install bower gulp-cli \
    && npm install \
    && bower install --allow-root\
    && gulp build

RUN find -maxdepth 1 ! -name 'dist' ! -name '.' -exec rm -rf {} \;
RUN chown -R www-data:www-data /app/dist

RUN apt-get purge -y \
    nodejs \
    build-essential \
    libssl-dev \
    git \
    && apt-get clean 

EXPOSE 80


CMD ["nginx"]

