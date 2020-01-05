FROM golang
MAINTAINER Nicolas Haunold <nicolas@haunold.me>

RUN go get github.com/bitly/statsdaemon
CMD ["statsdaemon", "-address=127.0.0.1:8125"]

EXPOSE 8125

