FROM golang:1.9-alpine

RUN apk add --no-cache git curl \
    && curl https://glide.sh/get | sh \
    && apk del --purge curl

ENTRYPOINT ["glide"]
CMD ["-v"]
