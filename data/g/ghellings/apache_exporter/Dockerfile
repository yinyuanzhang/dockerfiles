FROM golang:1.9-alpine

RUN \
  apk add --no-cache ca-certificates git && \
  mkdir /apache_exporter

ADD * /apache_exporter/

WORKDIR /apache_exporter

RUN go get github.com/prometheus/client_golang/prometheus && \
    go get github.com/sirupsen/logrus && \
    go get gopkg.in/alecthomas/kingpin.v2 && \ 
    env GOOS=linux GOARCH=amd64 go build .
EXPOSE 9117

ENTRYPOINT ["/apache_exporter/apache_exporter"]