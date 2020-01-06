FROM yobasystems/alpine-caddy

ADD caddy/live.conf /etc/Caddyfile
ADD site /home/caddy
WORKDIR /home/caddy
ADD site/js/built/min/cards_list.js /home/caddy/js/built/cards_list.js

EXPOSE 80
