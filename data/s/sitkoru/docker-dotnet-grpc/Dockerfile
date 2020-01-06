FROM mcr.microsoft.com/dotnet/core/sdk:2.2.105

ENV PROTOBUF_VERSION 3.7.0
ENV GRPC_VERSION v1.19.x

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN apt-get update \
    && apt-get install -y build-essential autoconf libtool pkg-config wget git unzip curl libatomic1 libgflags-dev apt-transport-https ca-certificates gnupg2 software-properties-common \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get install docker-ce-cli \
    && mkdir /tmp/protobuf \
    && cd /tmp/protobuf \
    && wget https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protoc-${PROTOBUF_VERSION}-linux-x86_64.zip \
    && unzip protoc-${PROTOBUF_VERSION}-linux-x86_64.zip \
    && chmod +x bin/protoc \
    && cp bin/protoc /usr/local/bin/protoc \
    && cp -a include /opt/ \
    && cd /tmp \
    && mkdir grpc \
    && git clone --recursive -b ${GRPC_VERSION} https://github.com/grpc/grpc \
    && cd grpc \
    && make \
    && make grpc_cli \
    && make install \
    && make install-grpc-cli \
    && rm -rf /tmp/* \
    && apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false build-essential autoconf libtool pkg-config unzip
