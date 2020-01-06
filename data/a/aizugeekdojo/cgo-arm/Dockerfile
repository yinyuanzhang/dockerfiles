FROM golang:latest

RUN apt update && apt install -y crossbuild-essential-armhf

ENV CC arm-linux-gnueabihf-gcc
ENV CXX arm-linux-gnueabihf-g++

ENV CGO_ENABLED 1
ENV GOOS linux
ENV GOARCH arm
