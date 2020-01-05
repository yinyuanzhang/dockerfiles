FROM golang:1.13.0-alpine3.10 AS build_image
RUN apk update && apk upgrade && \
    apk add --no-cache bash git gcc libc-dev make zip && \
    mkdir -p /go/src/github.com/fstab/grok_exporter
WORKDIR /go/src/github.com/fstab/grok_exporter
RUN wget https://github.com/kkos/oniguruma/releases/download/v6.7.0/onig-6.7.0.tar.gz && \
    tar xfz onig-6.7.0.tar.gz && \
    cd onig-6.7.0 && ./configure && make && make install
COPY . /go/src/github.com/fstab/grok_exporter
RUN /go/src/github.com/fstab/grok_exporter/release.sh dockerhub-linux-amd64

FROM alpine:3.7 as prod_image
COPY ./logstash-patterns-core /patterns
COPY --from=build_image /go/src/github.com/fstab/grok_exporter/dist/grok_exporter /
CMD /grok_exporter -config /config.yml
