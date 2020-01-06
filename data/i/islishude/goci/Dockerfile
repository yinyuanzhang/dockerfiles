FROM golang:1.13.5-alpine
ENV GO111MODULE on
RUN apk add --no-cache git ca-certificates build-base && rm -rf /var/cache/apk/*
RUN go get -u -v golang.org/x/lint/golint && \
    go get -u -v golang.org/x/tools/cmd/goimports && \
    wget -O- -nv https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s v1.21.0
CMD ["/bin/sh"]
