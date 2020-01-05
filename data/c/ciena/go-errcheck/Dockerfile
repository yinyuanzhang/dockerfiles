FROM golang:1.9
MAINTAINER David Bainbridge <dbainbri@ciena.com>
VOLUME /go/src
#RUN apk --update add git
RUN apt-get update -y && apt-get install -y git
WORKDIR /go
RUN go get -u github.com/kisielk/errcheck

COPY errcheck-entry-point /errcheck-entry-point
RUN chmod 755 /errcheck-entry-point
ENTRYPOINT [ "/errcheck-entry-point" ]
