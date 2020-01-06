FROM alpine

RUN apk add \
    openjdk8 \
    xmlstarlet \
    jq \
    && rm -rf /var/cache/apk/*

RUN addgroup -S app && adduser -S app -G app 

COPY ./start.sh /

RUN mkdir /server \
    && chown -R app:app /server \
    && chmod +x /start.sh

WORKDIR /server

VOLUME /server

ENTRYPOINT ["/start.sh"]

USER app

EXPOSE 25565
