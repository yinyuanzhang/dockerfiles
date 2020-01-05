FROM alpine:latest
RUN apk add --no-cache figlet
COPY entrypoint.sh /usr/local/bin
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
