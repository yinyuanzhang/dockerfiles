FROM miko2u/alpine

RUN cd /tmp \
 && apk add nginx logrotate --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
 && apk add shadow --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
 && find / -xdev -group nginx -exec chgrp 498 {} \; && groupmod -g 498 nginx \
 && find / -xdev -user nginx -exec chown 498 {} \; && usermod -u 498 nginx \
 && apk del shadow \
 && rm -rf /var/cache/apk/* \
 && mkdir -p /var/cache/nginx/cache \
 && mkdir -p /var/cache/nginx/tmp \
 && chown nginx:nginx /var/cache/nginx/cache \
 && chown nginx:nginx /var/cache/nginx/tmp \
 && mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.dist \
 && touch /var/log/messages \
 && mkdir -p /var/log/nginx \
 && ln -sf /dev/stdout /var/log/nginx/access.log \
 && ln -sf /dev/stderr /var/log/nginx/error.log

# config
COPY nginx.conf /etc/nginx/
COPY nginx.logrotate /etc/logrotate.d/nginx

# entry
COPY init prepare /boot/
