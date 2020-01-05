FROM golang:alpine as builder
COPY . /app
WORKDIR /app
RUN apk add --no-cache git \
    && go get github.com/BlueMonday/go-scryfall \
    && go get github.com/adammohammed/groupmebot \
    && apk del git
RUN go build -o app

FROM alpine
WORKDIR /app
COPY --from=builder /app/app /app/
COPY --from=builder /app/cfg.json /app/
COPY --from=builder /app/entrypoint.sh /app/
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
CMD ["./app"]

