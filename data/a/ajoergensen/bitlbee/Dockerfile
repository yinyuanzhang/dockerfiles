FROM ajoergensen/baseimage-alpine

RUN \
        apk -U add bitlbee bitlbee-otr bitlbee-facebook@testing

COPY root/ /

RUN \
        rm -rf /var/cache/apk/* /tmp/* && \
        chmod -v +x /etc/cont-init.d/* /etc/services.d/*/run

VOLUME [ "/var/lib/bitlbee" ]
