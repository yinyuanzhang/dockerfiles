FROM node:10.16.3-stretch


RUN npm config set unsafe-perm true \
&&  npm install -g grpc-tools 

RUN apt-get update \
&&  apt-get install -y unzip \
&&  apt-get clean

ENV GOPATH=/go
ENV PATH=/usr/local/go/bin:$GOPATH/bin:$PATH
RUN curl -sSL https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz | tar xvz -C /usr/local \
&&  mkdir -p $GOPATH && chmod 777 $GOPATH \
&&  cd /usr/local \
&&  curl -L -o protoc.zip https://github.com/protocolbuffers/protobuf/releases/download/v3.10.0/protoc-3.10.0-linux-x86_64.zip \
&&  unzip protoc.zip \
&&  go get github.com/golang/protobuf/protoc-gen-go \
&&  go get github.com/micro/protoc-gen-micro \
&&  rm -f protoc.zip \
&&  apt-get clean

RUN apt-get update \
&&  apt-get install -y python3-pip \
&&  pip3 install grpcio-tools \
&&  apt-get clean
