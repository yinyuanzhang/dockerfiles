FROM golang:1.12.4-alpine

EXPOSE 9130

RUN apk add --update --virtual git

COPY . /go/src/unifi_exporter
WORKDIR /go/src/unifi_exporter

RUN cd cmd/unifi_exporter && \
    GO111MODULE=on go install .

USER nobody
EXPOSE 9130/tcp
CMD ["unifi_exporter"]
