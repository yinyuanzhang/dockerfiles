FROM golang:1.9.2-alpine3.6

# Install git
RUN apk add --update git && rm -rf /var/cache/apk/*

# Get the stable version of gometalinter
RUN go get -v -u gopkg.in/alecthomas/gometalinter.v1 \
    && ln -s /go/bin/gometalinter.v1 /go/bin/gometalinter

# Install the linters
RUN gometalinter --install
