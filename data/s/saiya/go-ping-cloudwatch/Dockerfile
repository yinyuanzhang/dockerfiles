FROM golang:1.13-alpine3.10 AS builder

RUN apk add --no-cache git

COPY . /go/src/github.com/saiya/go-ping-cloudwatch
RUN go get github.com/saiya/go-ping-cloudwatch
RUN go install github.com/saiya/go-ping-cloudwatch

# --- Actual image --

FROM alpine:3.10

RUN apk add --no-cache libcap

COPY --from=builder /go/bin/go-ping-cloudwatch /usr/local/bin/go-ping-cloudwatch
RUN setcap cap_net_raw=+ep $(which go-ping-cloudwatch) && chmod +x $(which go-ping-cloudwatch)

ENTRYPOINT [ "go-ping-cloudwatch", "--privileged" ]
