FROM golang:1.10.4
WORKDIR /go/src/github.com/mandelsoft/dns-controller-manager/
RUN go get -u github.com/golang/dep/cmd/dep
COPY . .
RUN dep ensure
RUN CGO_ENABLED=0 GOOS=linux go build -a -o dns-controller-manager -ldflags "-X main.Version=$(cat VERSION)-$(git rev-parse HEAD)" ./cmd/dns

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/mandelsoft/dns-controller-manager/dns-controller-manager .
ENTRYPOINT ["./dns-controller-manager"]
