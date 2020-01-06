FROM golang:1.10.3

RUN apt-get update && \
    apt-get install -y unzip
RUN wget https://github.com/google/protobuf/releases/download/v3.5.1/protoc-3.5.1-linux-x86_64.zip
RUN unzip -o protoc-3.5.1-linux-x86_64.zip -d /usr/local bin/protoc

RUN wget https://github.com/edenhill/librdkafka/archive/v0.11.4.tar.gz && \
    tar -xvf v0.11.4.tar.gz && cd librdkafka-0.11.4 && \
    ./configure --prefix=/usr && \
    make && make install

RUN go get -u github.com/golang/protobuf/protoc-gen-go
