FROM ubuntu:trusty

RUN apt-get update -q && \
    apt-get install -y -q --no-install-recommends \
        cowsay

RUN ln -s /usr/games/cowsay /usr/bin

COPY . /test-cowsay
WORKDIR /test-cowsay
CMD ./test.sh
