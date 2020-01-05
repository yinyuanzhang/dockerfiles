FROM alpine:latest

RUN addgroup -S centrifugo && adduser -S -G centrifugo centrifugo \
    && mkdir /centrifugo && chown centrifugo:centrifugo /centrifugo \
    && mkdir /var/log/centrifugo && chown centrifugo:centrifugo /var/log/centrifugo

COPY ./config.json.example /centrifugo/config.json.example

ADD centrifugo /usr/bin/centrifugo
ADD start.sh /start.sh

RUN chmod +x /usr/bin/centrifugo
RUN chmod +x /start.sh

VOLUME ["/centrifugo", "/var/log/centrifugo"]

WORKDIR /centrifugo

USER centrifugo

CMD ["/start.sh"]

EXPOSE 8000
