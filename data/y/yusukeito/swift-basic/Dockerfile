FROM yusukeito/swift:swift5.1-dev

ENV PROTOC_VER 3.9.1

# 
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime

# Install dependency library
RUN apt-get update && \
    apt-get install -y libxml2-dev libmysqlclient-dev unzip libnghttp2-dev curl libssl-dev libcurl4-openssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install protoc
RUN curl -s -O -L https://github.com/google/protobuf/releases/download/v${PROTOC_VER}/protoc-${PROTOC_VER}-linux-x86_64.zip && \
    unzip protoc-${PROTOC_VER}-linux-x86_64.zip -d /usr && \
    rm protoc-${PROTOC_VER}-linux-x86_64.zip

# Build and install the swiftgrpc plugin
RUN git clone -b 1.0.0-alpha.7 --depth=1 https://github.com/grpc/grpc-swift && \
    cd grpc-swift && \
    make plugins && \
    cp ./.build/debug/protoc-gen-swift /usr/bin && \
    cp ./.build/debug/protoc-gen-grpc-swift /usr/bin && \
    cd ../ && rm -rf grpc-swift

