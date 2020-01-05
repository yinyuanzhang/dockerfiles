FROM golang:1.9

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get -qq install -y nodejs

RUN apt-get -qq install -y wget unzip ssh

RUN wget -nv https://github.com/google/protobuf/releases/download/v3.4.0/protoc-3.4.0-linux-x86_64.zip
RUN unzip -q protoc-3.4.0-linux-x86_64.zip -d protoc-3.4.0
RUN mv protoc-3.4.0/bin/protoc /usr/bin

RUN wget -nv https://github.com/github/hub/releases/download/v2.3.0-pre10/hub-linux-amd64-2.3.0-pre10.tgz
RUN tar -xzf hub-linux-amd64-2.3.0-pre10.tgz
RUN hub-linux-amd64-2.3.0-pre10/install

RUN curl -sL https://glide.sh/get | bash -

RUN go version
RUN node --version
RUN npm --version
RUN protoc --version
