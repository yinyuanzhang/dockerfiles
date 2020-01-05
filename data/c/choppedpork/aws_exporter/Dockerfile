FROM golang:alpine as builder

WORKDIR /go/src/aws_exporter
COPY . .

RUN apk --no-cache add git
RUN go get -d -v ./...
RUN go install -v ./...

FROM golang:alpine

COPY --from=builder /go/bin/aws_exporter /aws_exporter

ENTRYPOINT [ "/aws_exporter" ]
