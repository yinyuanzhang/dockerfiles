FROM golang:alpine AS builder

RUN apk add --no-cache curl git
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

RUN mkdir -p /go/src/github.com/emersion/emuarius
WORKDIR /go/src/github.com/emersion/emuarius

ADD . ./

RUN dep ensure -vendor-only
RUN ls vendor/github.com/emersion
RUN go build -o emuarius cmd/emuarius/main.go
RUN ls -la

FROM alpine
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY --from=builder /go/src/github.com/emersion/emuarius/emuarius /app/emuarius
RUN chmod +x emuarius
CMD ./emuarius
