FROM alpine:3.9

RUN apk add bash curl tcpdump util-linux coreutils ca-certificates

CMD ["sh", "-c", "trap : TERM INT; sleep infinity & wait"]
