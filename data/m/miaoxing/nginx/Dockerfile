FROM nginx:1-alpine

# https://github.com/docker-library/php/blob/66395400ad7735636d96cec62727e5ca7942370d/Dockerfile-alpine.template
# ensure www-data user exists
RUN set -x ; \
    addgroup -g 82 -S www-data ; \
    adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1
# 82 is the standard uid/gid for "www-data" in Alpine
# https://git.alpinelinux.org/aports/tree/main/apache2/apache2.pre-install?h=3.9-stable
# https://git.alpinelinux.org/aports/tree/main/lighttpd/lighttpd.pre-install?h=3.9-stable
# https://git.alpinelinux.org/aports/tree/main/nginx/nginx.pre-install?h=3.9-stable

# Remove the default conf to avoid conflict
RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx.conf ./server-common.conf ./enable-ssl.conf ./enable-ssl-legacy.conf /etc/nginx/
