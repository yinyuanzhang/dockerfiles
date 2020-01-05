FROM golang:1.7.3-alpine

RUN mkdir -p /go/src/gophish \
    && mkdir -p /go/src/github.com/gophish/gophish
WORKDIR /go/src/gophish
COPY . /go/src/gophish
COPY . /go/src/github.com/gophish/gophish

RUN apk --no-cache add --virtual build-dependencies \
    git \
    g++ \
    && go get -d -v ./... \
    && go build -v gophish.go \
    && apk del build-dependencies

CMD ["./gophish"]

EXPOSE 3333 80
