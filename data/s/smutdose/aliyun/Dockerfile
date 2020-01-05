FROM alpine:3.10
RUN apk add --update --no-cache curl
RUN curl -s https://aliyuncli.alicdn.com/aliyun-cli-linux-3.0.20-amd64.tgz | tar xz -C /usr/local/bin

FROM alpine:3.10
COPY --from=0 /usr/local/bin /usr/local/bin
