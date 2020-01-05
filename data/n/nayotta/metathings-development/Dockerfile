FROM golang:1.12-alpine

RUN apk add git make gcc libc-dev protobuf
RUN git clone https://github.com/protocolbuffers/protobuf.git --depth 1 && \
    cd protobuf/src && \
    mkdir -p /usr/local/include && \
    cp -r google /usr/local/include && \
    cd ~ && \
    rm -rf protobuf
RUN go get github.com/golang/protobuf/proto && \
    go get github.com/golang/protobuf/protoc-gen-go && \
    go get github.com/mwitkow/go-proto-validators/protoc-gen-govalidators && \
    go get github.com/casbin/casbin-server/proto
