FROM swift:4.1

MAINTAINER muukii <muukii.app@gmail.com>

WORKDIR /local

RUN apt-get -q update
RUN apt-get -q install -y zip unzip wget

ENV TAG "1.1.0"

RUN git clone --depth=1 -b $TAG https://github.com/apple/swift-protobuf.git
RUN cd ./swift-protobuf && swift build -c release # -Xswiftc -static-stdlib
RUN cp ./swift-protobuf/.build/x86_64-unknown-linux/release/protoc-gen-swift /usr/local/bin/protoc-gen-swift

RUN wget https://github.com/google/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_64.zip -O protobuf.zip
RUN unzip protobuf.zip -d ./protobuf
RUN rm -rf protobuf.zip
RUN cp ./protobuf/bin/protoc /usr/local/bin/protoc

ADD . /proto
WORKDIR /proto

ENTRYPOINT ["protoc"]
