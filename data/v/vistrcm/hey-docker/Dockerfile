# build application phase
FROM golang:1.11 as builder

RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go get -u github.com/rakyll/hey

# build image
FROM scratch
COPY --from=builder /go/bin/hey /hey
# array in etrypoint is a dirty hack to be able to pass parameters via CMD later
ENTRYPOINT ["/hey"]
