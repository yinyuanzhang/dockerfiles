FROM ubuntu:trusty

RUN apt-get update && apt-get install fonttools -y

COPY codes.sh /usr/bin/charcodes

ENTRYPOINT ["charcodes"]
