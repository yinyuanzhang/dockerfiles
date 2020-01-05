FROM golang:latest
ENV GOPATH /usr/local/goCep
RUN apt-get update \
	&& apt-get install -y pkg-config  libcurl4-openssl-dev \
	&& cd /usr/local \
	&& git clone https://github.com/eminetto/goCep.git \
	&& cd goCep \
	&& go get github.com/go-martini/martini \
	&& go get github.com/andelf/go-curl \
	&& go get github.com/ryanuber/go-filecache \
	&& go build

EXPOSE 3000

CMD ["/usr/local/goCep/goCep"]	