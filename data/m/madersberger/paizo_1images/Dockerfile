FROM "golang:alpine"

WORKDIR /go/src
COPY . /go/src
RUN apk add --no-cache --virtual .build-deps git gcc musl-dev make && export GO111MODULE=on && cd /go/src && go build -o main
ENTRYPOINT ["/go/src/main"]
EXPOSE 9080