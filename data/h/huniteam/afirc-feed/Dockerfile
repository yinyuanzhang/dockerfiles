FROM nginx:1.13-alpine

RUN rm -f /usr/share/nginx/html/*
ADD data/afirc /usr/share/nginx/html
ADD default.conf /etc/nginx/conf.d/default.conf
