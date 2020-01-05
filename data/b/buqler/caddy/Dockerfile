FROM golang:1.12-alpine3.10 AS build
WORKDIR /app
RUN apk add git
COPY . .
RUN go build


FROM alpine:3.10
WORKDIR /app
RUN apk --no-cache add ca-certificates
COPY --from=build /app/caddy /usr/local/bin/caddy

VOLUME /root/.caddy
EXPOSE 80 443 2015
ENTRYPOINT ["caddy", "-agree"]
