FROM golang:1.12.6-alpine

LABEL "io.cycloid"="Cycloid" \
      "description"="A docker image with the versions of go & tools that we use on each moment that the image is built" \
      "reference"="https://www.cycloid.io" \
      "maintainer"="contact@cycloid.io"

RUN apk add build-base curl git npm

ENV GOBIN /go/bin
ENV GOPATH /go
ENV GO111MODULE on
ENV GOFLAGS "-mod=vendor"
COPY vendor ${GOPATH}/src/

RUN mkdir -p ${GOBIN} && \
 	GO111MODULE=off && \
    go install golang.org/x/lint/golint && \
    go install golang.org/x/tools/cmd/goimports && \
    go install golang.org/x/tools/cmd/stringer && \
    go install github.com/golang/mock/mockgen && \
    go install github.com/alvaroloes/enumer && \
    go install github.com/hexdigest/gowrap/cmd/gowrap && \
    go build -tags 'mysql' -o ${GOBIN}/migrate  github.com/golang-migrate/migrate/cli && \
    go install github.com/TykTechnologies/go-bindata/go-bindata && \
    go install github.com/cycloidio/html2txt && \
    curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s -- -b $(go env GOPATH)/bin v1.17.1 && \
    cd ${GOPATH} && rm -rf src pkg && mkdir src && \
    npm install -g mjml