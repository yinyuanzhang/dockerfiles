FROM alpine

LABEL Justin Tien <thitbbeb@gmail.com>

RUN apk --update add jq && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

VOLUME /jq
WORKDIR /jq

ENTRYPOINT ["jq"]
CMD ["--help"]