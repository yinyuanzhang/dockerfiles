FROM ubuntu:18.04

WORKDIR /fuchsia

RUN apt-get update && apt-get -y install build-essential curl git python unzip && curl -s "https://fuchsia.googlesource.com/scripts/+/master/bootstrap?format=TEXT" | base64 --decode | bash
