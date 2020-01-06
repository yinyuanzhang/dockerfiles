FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install golang && \
    apt-get -y install git && \
    go get github.com/lib/pq

COPY . .

EXPOSE 5000

CMD go test