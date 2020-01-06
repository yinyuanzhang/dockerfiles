FROM psaudio/alpine-base as base

FROM httpd:2.4-alpine

COPY --from=base /usr/ /usr/

COPY mime.types /usr/local/apache2/conf/mime.types
COPY override_me.conf /usr/local/apache2/conf/httpd.conf