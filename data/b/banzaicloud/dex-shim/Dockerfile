FROM golang:1.12-alpine
ENV GO111MODULE=on
RUN apk add --update git
RUN go get github.com/dexidp/dex/cmd/example-app@v2.21.0


FROM quay.io/dexidp/dex:v2.21.0
COPY web /web
COPY --from=0 /go/bin/example-app /usr/local/bin/example-app
