# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang:latest

COPY . $GOPATH/src/github.com/korshunovgo/proto/grpc
WORKDIR $GOPATH/src/github.com/korshunovgo/proto/grpc/service
#get dependancies
RUN go get -d -v
#build the binary
RUN go install github.com/korshunovgo/proto/grpc/service

# Run the outyet command by default when the container starts.
ENTRYPOINT $GOPATH/bin/service

# Document that the service listens on port 8888.
EXPOSE 8888