FROM alpine:3.5

#
# BASE PACKAGES
#
RUN apk add --no-cache \
            bash \
            xmlstarlet \
            librsvg && \
    ln -s /usr/bin/rsvg-convert /usr/local/bin/rsvg && \
    addgroup -g 10777 xmlworker && \
    adduser -D -G xmlworker -u 10777 xmlworker && \
    mkdir /icons/ && \
    chown xmlworker:xmlworker /icons

#
# RUN
#
USER xmlworker
VOLUME ["/icons/"]
WORKDIR /icons/
CMD ["rsvg", "--version"]