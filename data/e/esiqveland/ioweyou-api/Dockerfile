FROM golang:1.4.2

# taken from: https://github.com/docker-library/golang/blob/c1baf037d71331eb0b8d4c70cff4c29cf124c5e0/1.4/onbuild/Dockerfile

RUN mkdir -p /go/src/github.com/esiqveland/ioweyou-api
WORKDIR /go/src/github.com/esiqveland/ioweyou-api

# this will ideally be built by the ONBUILD below ;)
CMD ["go-wrapper", "run"]

COPY . /go/src/github.com/esiqveland/ioweyou-api
COPY conf/conf-deploy.yml /go/src/github.com/esiqveland/ioweyou-api/conf.yml

RUN go-wrapper download
RUN go-wrapper install
