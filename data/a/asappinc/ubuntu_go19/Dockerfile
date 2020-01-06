FROM asappinc/ubuntu:16.04.0

RUN cd / && curl -OL https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz
RUN echo "de874549d9a8d8d8062be05808509c09a88a248e77ec14eb77453530829ac02b *go1.9.2.linux-amd64.tar.gz" | sha256sum -c -
RUN tar -zxvf go1.9.2.linux-amd64.tar.gz
RUN rm go1.9.2.linux-amd64.tar.gz

RUN mkdir -p /go-path
ENV GOPATH /go-path
ENV GOROOT /go
ENV PATH ${PATH}:/usr/local/bin:$GOROOT/bin
WORKDIR /go

#protobufs
RUN set -ex && \
    curl -OL https://github.com/google/protobuf/releases/download/v3.4.0/protoc-3.4.0-linux-x86_64.zip && \
    unzip protoc-3.4.0-linux-x86_64.zip -d protoc-3.4.0 && \
    mv protoc-3.4.0/bin/protoc /usr/local/bin && \
    rm -rf protoc-3.4.0 protoc-3.4.0-linux-x86_64.zip && \
    go get github.com/golang/protobuf/protoc-gen-go && \
    go build github.com/golang/protobuf/protoc-gen-go && \
    mv protoc-gen-go /usr/local/