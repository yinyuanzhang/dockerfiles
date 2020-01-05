FROM golang:1.10.0-stretch

ENV PACKAGES "git make zip bash curl"

RUN apt-get update && apt-get -y install $PACKAGES && apt-get clean
