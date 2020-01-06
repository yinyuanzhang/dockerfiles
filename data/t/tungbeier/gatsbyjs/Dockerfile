FROM alpine:3.9.4

LABEL name="tungbeier alpine image for gatsbyjs" \
    maintainer="tung beier <beier.tung@web.de>" \
    summary="Alpine image to serve a website with gatsbyjs"

EXPOSE 8000

RUN apk update --no-cache && \
        apk upgrade --no-cache && \
        apk add --no-cache npm git python make g++ && \
        apk add vips-dev fftw-dev --no-cache \
        --repository http://dl-3.alpinelinux.org/alpine/edge/community \
        --repository http://dl-3.alpinelinux.org/alpine/edge/main && \
        rm -fR /var/cache/apk/* && \
        npm install -g gatsby-cli yarn

COPY ./init.sh /init.sh
RUN chmod +x /init.sh && \
        adduser -h /app -G wheel -D developer && \
        chown developer:wheel /init.sh

USER developer

WORKDIR /app
VOLUME ["/app"]

ENTRYPOINT ["/init.sh"]

