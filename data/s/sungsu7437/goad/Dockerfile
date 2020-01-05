FROM golang:1.8.1-stretch

RUN apt-get update
RUN apt-get install -y zip
RUN git clone https://github.com/sungsu7437/goad.git /go/src/github.com/goadapp/goad
WORKDIR /go/src/github.com/goadapp/goad
RUN go get -u github.com/jteeuwen/go-bindata/...
RUN make install

EXPOSE 8080
