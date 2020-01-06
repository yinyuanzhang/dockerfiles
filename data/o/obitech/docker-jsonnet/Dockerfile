# Step 1: Build jsonnet from source
FROM golang:alpine as builder

RUN apk add --no-cache git
RUN go get github.com/google/go-jsonnet/jsonnet \
    && cd /go/src/github.com/google/go-jsonnet/jsonnet \
    && go build

# Step 2: Copy binary
FROM golang:alpine
COPY --from=builder /go/src/github.com/google/go-jsonnet/jsonnet/jsonnet /usr/local/bin
RUN chmod +x /usr/local/bin/jsonnet

WORKDIR /workdir
ENTRYPOINT ["jsonnet"]
CMD ["-h"]

VOLUME /workdir