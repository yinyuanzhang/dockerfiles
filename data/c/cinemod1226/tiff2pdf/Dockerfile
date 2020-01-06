FROM golang:1.13


WORKDIR /go/src/convert2pdf

COPY . .

RUN apt-get update && apt-get install -y libtiff-tools

EXPOSE 8090

CMD ./convert2pdf
