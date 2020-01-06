FROM golang:alpine

RUN apk --no-cache add git

ADD . "$GOPATH/src/yaml2json"

RUN go get github.com/ghodss/yaml
RUN go install yaml2json

FROM alpine:latest

WORKDIR /bin/

COPY --from=0 /go/bin/yaml2json .

ENTRYPOINT ["/bin/yaml2json"]
