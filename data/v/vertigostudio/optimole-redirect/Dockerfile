FROM alpine:edge

ENV GOPATH /go
ENV PATH /usr/local/go/bin:$PATH

ADD . /go/src/github.com/Codeinwp/optimole-redirecter
WORKDIR /go/src/github.com/Codeinwp/optimole-redirecter

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
  && apk --no-cache upgrade \
  && apk add --no-cache curl ca-certificates go gcc g++ make musl-dev fftw-dev glib-dev expat-dev \
  && rm -rf /var/cache/apk*

RUN cd /go/src/github.com/Codeinwp/optimole-redirecter \
  && CGO_LDFLAGS_ALLOW="-s|-w" go build -v -o /usr/local/bin/optimole-redirecter


CMD ["optimole-redirecter"]

EXPOSE 8080