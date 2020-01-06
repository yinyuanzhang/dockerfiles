FROM alpine:3.8

LABEL maintainer Justin Liu <justintwd@gmail.com>

RUN apk --update add --no-cache curl git jq wget bash && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apk/*

CMD [ "tail", "-f", "/dev/null" ]
