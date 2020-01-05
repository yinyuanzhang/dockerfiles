FROM golang:1.10-alpine AS build

WORKDIR /usr/local/go/src/github.com/percona/mongodb_exporter/
ADD . /usr/local/go/src/github.com/percona/mongodb_exporter/

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /app

FROM quay.io/prometheus/busybox:latest

COPY --from=build /app /bin/mongodb_exporter

EXPOSE 9216
ENTRYPOINT  [ "/bin/mongodb_exporter" ]