# use base image for shim
FROM hyperledger/fabric-baseimage:latest AS baseimage

RUN go get github.com/hyperledger/fabric || true && cd $GOPATH/src/github.com/hyperledger/fabric && mkdir -p build && sed -i 's/EXECUTABLES = go docker git curl/EXECUTABLES = go/g' Makefile && make build/goshim.tar.bz2

FROM golang:1.10.3
# cheers :)
MAINTAINER Dmitry Zhvakin <dm@hostdm.ru>
# add shim from build
COPY --from=baseimage /opt/gopath/src/github.com/hyperledger/fabric/build/goshim.tar.bz2 ${GOPATH}/src/
# add build dependencies
RUN apt update && \
    apt install -y libtool
# from official fabric-ccenv image
RUN mkdir -p /chaincode/input /chaincode/output
