FROM ubuntu:xenial
LABEL maintainer "Sosuke Moriguchi"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y && \
  apt-get install -y wget make git ocaml ocaml-native-compilers camlp5 ocaml-findlib
