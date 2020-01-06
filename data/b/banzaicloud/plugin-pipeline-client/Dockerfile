FROM golang:1.10-alpine

ADD . /go/src/github.com/banzaicloud/drone-plugin-pipeline-client
WORKDIR /go/src/github.com/banzaicloud/drone-plugin-pipeline-client
RUN go build -o /bin/pipeline-client .

FROM alpine:3.7

RUN apk --update --no-cache add ca-certificates
COPY --from=0 /bin/pipeline-client /bin
ENTRYPOINT ["/bin/pipeline-client"]
