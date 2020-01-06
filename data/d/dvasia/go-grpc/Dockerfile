FROM golang:1.10

ENV PB_VER 3.5.1
ENV PB_URL https://github.com/google/protobuf/releases/download/v${PB_VER}/protoc-${PB_VER}-linux-x86_64.zip
ENV PACKAGES="install unzip jq curl"

RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get clean \
    \
    && echo "-- Install protoc" \
    \
    && mkdir -p /tmp/protoc \
    && curl -L ${PB_URL} > /tmp/protoc/protoc.zip \
    && cd /tmp/protoc \
    && unzip protoc.zip \
    && cp /tmp/protoc/bin/protoc /usr/local/bin \
    && cp -R /tmp/protoc/include/* /usr/local/include \
    && chmod go+rx /usr/local/bin/protoc \
    && cd /tmp \
    && rm -r /tmp/protoc \
    \
    && set -x \
    && echo "Install grpc things" \
    \
    && go get google.golang.org/grpc \
    && go get github.com/golang/protobuf/protoc-gen-go \
    \
    && echo "Install protoc plugins" \
    \
    && go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway \
    && go get -u github.com/grpc-ecosystem/grpc-gateway/... \
    && (go get -u github.com/googleapis/googleapis || stat ${GOPATH}/src/github.com/googleapis/googleapis/google) \
    && go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger \
    \
    && echo "Instal golang tools" \
    && go get -u github.com/golang/dep/cmd/dep \
    && go get -u github.com/golang/lint/golint \
    && go get -u github.com/wadey/gocovmerge \
    && go get -u github.com/axw/gocov/... \
    && go get -u github.com/AlekSi/gocov-xml \
    && go get -u github.com/tebeka/go2xunit \
    && go get -u github.com/jteeuwen/go-bindata/... \
    && go get -u -d github.com/mattes/migrate/cli github.com/go-sql-driver/mysql \
    && go build -tags 'mysql' -o ${GOPATH}/bin/migrate github.com/mattes/migrate/cli \
    \
    && rm -rf /var/lib/apt/lists/*



