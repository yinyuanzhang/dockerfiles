FROM golang:1.12-alpine as builder
RUN apk add --no-cache git
RUN mkdir -p /go/src/github.com/meatballhat/lildyndns
WORKDIR /go/src/github.com/meatballhat/lildyndns
COPY . .
ENV CGO_ENABLED 0
ENV GO111MODULE on
RUN go get -d -v ./...
RUN go install -v ./...

FROM alpine:latest
RUN apk --no-cache add ca-certificates curl bash
RUN mkdir -p /usr/local/bin
COPY --from=builder /go/bin/lildyndns /usr/local/bin/lildyndns
CMD ["/usr/local/bin/lildyndns"]
