FROM ubuntu:18.04

MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>

RUN apt-get update && apt-get upgrade -y

RUN apt-get install curl gnupg bzip2 make g++ -y && curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install nodejs -y

RUN apt-get install git wget openssl -y