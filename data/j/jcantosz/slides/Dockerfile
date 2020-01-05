FROM golang:1.11 as build

RUN go get -d -v github.com/bketelsen/slides
RUN go build -o /go/bin/slides  github.com/bketelsen/slides
RUN chmod +x /go/bin/slides

FROM debian:9.5-slim
COPY --from=build /go/bin/slides /usr/local/bin

WORKDIR /slides
ENTRYPOINT [ "/usr/local/bin/slides" ]
