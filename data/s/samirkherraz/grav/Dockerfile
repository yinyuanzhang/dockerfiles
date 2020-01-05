FROM samirkherraz/alpine-s6

RUN set -x \
    && apk --no-cache add memcached php7 php7-fpm php7-curl php7-ctype php7-dom php7-gd php7-json php7-mbstring php7-openssl php7-session php7-simplexml php7-xml php7-zip php7-memcached php7-yaml php7-ldap 

RUN set -x \
    && apk --no-cache add nginx \
    && mkdir -p /run/nginx/ \
    && rm -R /var/www/* || true \
    && chown nginx:nginx /var/www/ /run/nginx/



RUN set -x \
    && rm /etc/nginx/conf.d/* \
    && rm /etc/php7/php-fpm.d/* 

ADD conf/ /

RUN set -x \
    && chmod +x /etc/cont-init.d/* \
    && chmod +x /etc/s6/services/*/*
