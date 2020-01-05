FROM nginx:latest

MAINTAINER Daniel Toth <firius87@gmail.com>

RUN apt-get update && apt-get upgrade -y

RUN apt-get autoremove -y && apt-get autoclean -y && rm -rf /var/lib/apt/lists/*

COPY ./options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf

RUN rm -Rf /etc/nginx/conf.d/default.conf /usr/share/nginx/html
