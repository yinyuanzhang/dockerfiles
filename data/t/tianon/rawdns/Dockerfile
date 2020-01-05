FROM golang:1.11-alpine3.8

RUN apk add --no-cache ca-certificates openssl

ENV GB_VERSION 0.4.2
RUN set -x \
	&& mkdir -p /go/src/github.com/constabulary \
	&& cd /go/src/github.com/constabulary \
	&& wget -qO- "https://github.com/constabulary/gb/archive/v${GB_VERSION}.tar.gz" \
		| tar -xz \
	&& mv gb-* gb \
	&& cd gb \
	&& go install -v ./...

WORKDIR /usr/src/rawdns
ENV PATH /usr/src/rawdns/bin:$PATH

COPY . .
RUN gb build -ldflags '-s -w'

CMD ["rawdns"]
