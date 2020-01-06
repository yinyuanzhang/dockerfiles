FROM golang:alpine

RUN mkdir /proto

RUN mkdir /stubs

RUN apk -U --no-cache add git protobuf nginx openssl

RUN go get -u -v github.com/golang/protobuf/protoc-gen-go \
	github.com/mitchellh/mapstructure \
	google.golang.org/grpc \
	google.golang.org/grpc/reflection \
	golang.org/x/net/context \
	github.com/go-chi/chi \
	github.com/renstrom/fuzzysearch/fuzzy \
	golang.org/x/tools/imports

RUN go get -u -v github.com/gobuffalo/packr/v2/... \
                 github.com/gobuffalo/packr/v2/packr2

# cloning well-known-types
RUN git clone https://github.com/google/protobuf.git /protobuf-repo

RUN mkdir protobuf

# only use needed files
RUN mv /protobuf-repo/src/ /protobuf/

RUN rm -rf /protobuf-repo

RUN apk del git

RUN mkdir -p /go/src/github.com/tokopedia/gripmock

COPY . /go/src/github.com/tokopedia/gripmock

WORKDIR /go/src/github.com/tokopedia/gripmock/protoc-gen-gripmock

RUN packr2

# install generator plugin
RUN go install -v

RUN packr2 clean

WORKDIR /go/src/github.com/tokopedia/gripmock

# install gripmock
RUN go install -v

RUN rm -rf *

# NGINX and SSL configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /root/

EXPOSE 4770 4771 80 443

ENTRYPOINT ["/root/entrypoint.sh"]
