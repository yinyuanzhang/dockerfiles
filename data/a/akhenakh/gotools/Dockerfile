FROM golang:1.13-stretch
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common protobuf-compiler 
RUN add-apt-repository ppa:masterminds/glide &&  apt-get install -y --no-install-recommends golang-glide 

RUN GIT_TAG="v1.2.0"  && go get -d -u github.com/golang/protobuf/protoc-gen-go && \
    git -C "$(go env GOPATH)"/src/github.com/golang/protobuf checkout $GIT_TAG && \
    go install github.com/golang/protobuf/protoc-gen-go

RUN curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s -- -b $(go env GOPATH)/bin v1.20.0

RUN GODEP_VERSION=v0.5.1 && \
    wget -qO/bin/dep https://github.com/golang/dep/releases/download/${GODEP_VERSION}/dep-linux-amd64 && \
    chmod +x /bin/dep

RUN GRPC_HEALTH_PROBE_VERSION=v0.2.1 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

RUN GRPC_GATEWAY_VERSION=v1.8.5 && \
    wget -qO/bin/protoc-gen-grpc-gateway https://github.com/grpc-ecosystem/grpc-gateway/releases/download/${GRPC_GATEWAY_VERSION}/protoc-gen-grpc-gateway-${GRPC_GATEWAY_VERSION}-linux-x86_64 && \
    chmod a+x /bin/protoc-gen-grpc-gateway && \
    wget -qO/bin/protoc-gen-swagger https://github.com/grpc-ecosystem/grpc-gateway/releases/download/${GRPC_GATEWAY_VERSION}/protoc-gen-swagger-${GRPC_GATEWAY_VERSION}-linux-x86_64 && \
    chmod a+x /bin/protoc-gen-swagger

RUN go get github.com/google/wire/cmd/wire

RUN go get github.com/vektra/mockery/.../

RUN go get github.com/gobuffalo/packr/packr

RUN mkdir /builder

COPY go_workspace.go prepare_workspace.inc /builder/

COPY run.bash /bin/

ENTRYPOINT ["run.bash"]
