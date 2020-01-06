FROM golang:alpine as build
RUN apk update \
    && apk add git make

RUN go get github.com/digitalocean/bind_exporter
WORKDIR /go/src/github.com/digitalocean/bind_exporter
RUN make

FROM alpine
COPY --from=build /go/src/github.com/digitalocean/bind_exporter/bind_exporter .

CMD ./bind_exporter
