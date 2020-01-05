FROM golang:1.10-alpine
RUN apk add --update git
RUN go get -v github.com/ryodocx/oauth2_proxy

FROM alpine:3.8
WORKDIR /opt
COPY  --from=0 /etc/ssl/certs /etc/ssl/certs
COPY  --from=0 /go/bin/oauth2_proxy /usr/local/bin/oauth2_proxy
CMD ["oauth2_proxy"]
