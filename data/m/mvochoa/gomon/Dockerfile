FROM golang:1.11-alpine3.8

RUN apk update && apk add git gcc bind-dev musl-dev
RUN go get github.com/mvochoa/CompileDaemon
RUN go install /go/src/github.com/mvochoa/CompileDaemon
RUN chmod +x /go/bin/CompileDaemon
RUN mv /go/bin/CompileDaemon /usr/local/bin/gomon
RUN rm -Rf github.com golang.org

ENV GO111MODULE=on

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sh", "/usr/local/bin/docker-entrypoint.sh"]