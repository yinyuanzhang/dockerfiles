# This image includes osxcross and mingw to be able to compile CGO enabled Go code on OSX and Windows
FROM dockercore/golang-cross

RUN apt-get install make git g++
RUN go get -u github.com/golang/dep/cmd/dep && \
  cp /go/bin/dep /usr/local/bin/dep
