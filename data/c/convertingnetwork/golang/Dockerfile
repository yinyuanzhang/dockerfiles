FROM golang:1
ADD . /
RUN go get -u github.com/golang/dep/cmd/dep && \
    go get -u github.com/go-swagger/go-swagger/cmd/swagger && \
    go get -u github.com/derekparker/delve/cmd/dlv && \
    go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway && \
    go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger && \
    go get -u github.com/golang/protobuf/protoc-gen-go && \
    go get -u github.com/mwitkow/go-proto-validators/protoc-gen-govalidators && \
    go get -u github.com/tebeka/go2xunit && \
    go get -u gotest.tools/gotestsum
ENV GO111MODULE=on
ENV GOFLAGS=-mod=vendor
ENV GOOS=linux
ENV CGO_ENABLED=1

# force build!
