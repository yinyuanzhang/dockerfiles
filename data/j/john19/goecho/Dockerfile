# FROM golang
# WORKDIR /go/src/github.com/nkex606/docker-trigger/
# COPY . .
# RUN go get -d -v -t ./...
# RUN go test && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o goecho .
# CMD ["./goecho"]

FROM golang AS builder
WORKDIR /go/src/github.com/nkex606/docker-trigger/
COPY . .
RUN go get -d -v -t ./...
RUN go test && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o goecho .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/nkex606/docker-trigger/goecho .
CMD ["./goecho"]
