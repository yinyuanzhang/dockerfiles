FROM alpine

RUN apk add --update nginx \
    && rm -rf /var/cache/apk/* \
    && wget https://github.com/hivemq/hivemq-mqtt-web-client/archive/master.zip \
    && unzip master.zip \
    && mv hivemq-mqtt-web-client-master hivemq-mqtt-web-client \
    && rm master.zip

ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx"]
