FROM golang:1.11-alpine3.8 AS builder
RUN apk add --no-cache make git
WORKDIR /go/src/github.com/kakakakakku/gin-example/
COPY . .
RUN go get github.com/gin-gonic/gin && go build

FROM alpine:3.8
RUN apk add --no-cache ca-certificates
COPY --from=builder /go/src/github.com/kakakakakku/gin-example/gin-example .
ENTRYPOINT ["./gin-example"]
