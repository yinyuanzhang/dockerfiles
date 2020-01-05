FROM ubuntu:18.04

ADD https://mirror.racket-lang.org/installers/7.4/racket-7.4-x86_64-linux.sh /tmp

WORKDIR /tmp

RUN sh racket-7.4-x86_64-linux.sh --unix-style --create-dir --dest /usr/

WORKDIR /code
