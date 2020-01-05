FROM golang:1.12

ENV PORT 8082
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN go get github.com/fullstorydev/grpcui
RUN go install github.com/fullstorydev/grpcui/cmd/grpcui

# Install protoc-gen-grpc for common-protos
RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway

# Install protoc-gen-go, protoc-gen-grpc-gateway, protoc-gen-swagger
RUN go install github.com/golang/protobuf/protoc-gen-go/ \
    github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway


EXPOSE ${PORT}

CMD grpcui ${PROTOSET_OPTIONS} -bind 0.0.0.0 -port ${PORT} -plaintext ${URL}
