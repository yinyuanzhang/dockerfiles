FROM nginx
MAINTAINER gsh

ENV http_proxy="http://proxy.houston.hpecorp.net:8080"
ENV https_proxy="http://proxy.houston.hpecorp.net:8080"

COPY content /usr/share/nginx/html

VOLUME  /usr/share/nginx/html
