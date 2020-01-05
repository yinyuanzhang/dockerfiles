FROM alpine as certs
RUN apk update && apk add ca-certificates

FROM busybox:glibc
COPY --from=certs /etc/ssl/certs /etc/ssl/certs
RUN wget https://github.com/dropbox/dbxcli/releases/download/v3.0.0/dbxcli-linux-amd64 \
  && chmod +x dbxcli-linux-amd64 \
  && mv dbxcli-linux-amd64 /bin/dbxcli
