# STAGE0
FROM golang:latest as builder

MAINTAINER Christian Sakshaug <christian@sakshaug.net>

ENV SERVER_ADDRESS :8080

COPY . /go/src/http_debug_server/
WORKDIR /go/src/http_debug_server/
RUN go get
RUN rm -rf /go/src/github.com/csakshaug/http_debug_server
RUN make
RUN mkdir /app
RUN mv bin/http_debug_server-linux-amd64 /app/http_debug_server
RUN chmod 755 /app/http_debug_server

FROM alpine
COPY --from=builder /app /app

WORKDIR /app

CMD ["/app/http_debug_server", "--server", "--address $SERVER_ADDRESS"]
