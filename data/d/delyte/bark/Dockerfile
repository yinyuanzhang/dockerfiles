FROM golang:1.11.5-alpine3.8
MAINTAINER delyte wang <wangyouqian@gmail.com> 

RUN apk update && apk add --no-cache build-base gcc git wget \
	&& go get -u github.com/golang/dep/cmd/dep

COPY . /go/src/project/

WORKDIR /go/src/project/

RUN dep ensure && make build

EXPOSE 80

ENTRYPOINT ["make","start"]
