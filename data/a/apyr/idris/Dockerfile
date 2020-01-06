FROM ubuntu:18.04

RUN apt update && apt install -y nano build-essential zlib1g-dev cabal-install

RUN cabal update
RUN cabal install idris

ENV PATH="/root/.cabal/bin:${PATH}"
