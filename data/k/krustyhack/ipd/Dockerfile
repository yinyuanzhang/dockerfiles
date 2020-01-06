FROM golang:1.6

RUN apt-get update && \
	apt-get install -y git
WORKDIR /go/src/app
RUN git clone https://github.com/KrustyHack/ipd.git . && \
	go get github.com/martinp/ipd
EXPOSE 8080
CMD ["ipd", "--trusted-header=X-Real-IP"]
