FROM alpine:3.6 as builder

RUN apk add --no-cache wget

WORKDIR /fonts

RUN wget ftp://ftp.figlet.org/pub/figlet/fonts/contributed/*

FROM alpine:3.6

RUN apk add --no-cache figlet

COPY --from=builder /fonts/* /usr/share/figlet/fonts/

ENTRYPOINT ["figlet"]