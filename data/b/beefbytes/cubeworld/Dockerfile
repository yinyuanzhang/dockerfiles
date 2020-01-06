FROM ubuntu:18.04

RUN apt update
RUN apt-get install -y curl git build-essential libsqlite3-dev libssl-dev libbz2-dev libreadline-dev zlib1g-dev

WORKDIR /mnt/cuwo
RUN curl -L https://git.io/vFLZX | bash

ENTRYPOINT ./run_server.sh