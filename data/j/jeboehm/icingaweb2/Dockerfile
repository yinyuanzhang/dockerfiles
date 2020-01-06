FROM jeboehm/php-nginx-base:7.2

ARG VER=2.6.1
ENV TIMEZONE=Europe/Berlin

RUN apk --no-cache add gettext-dev && \
    docker-php-ext-install gettext && \
    apk --no-cache del gettext-dev

RUN wget -qO /tmp/icingaweb2.zip https://github.com/Icinga/icingaweb2/archive/v${VER}.zip && \
    unzip -d /usr/share /tmp/icingaweb2.zip && \
    rm -f /tmp/icingaweb2.zip && \
    ln -sf /usr/share/icingaweb2-${VER} /usr/share/icingaweb2 && \
    ln -sf /usr/share/icingaweb2-${VER}/bin/icingacli /usr/bin/icingacli && \
    addgroup icingaweb2 && \
    adduser www-data icingaweb2 && \
    /usr/bin/icingacli setup config directory --group icingaweb2

COPY nginx.conf /etc/nginx/sites-enabled/10-docker.conf
COPY entrypoint.sh /usr/bin/entrypoint.sh

VOLUME [ "/etc/icingaweb2" ]

CMD [ "/usr/bin/entrypoint.sh" ]
