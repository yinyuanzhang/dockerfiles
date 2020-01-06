FROM ubuntu:18.04

RUN apt-get update && apt-get -y upgrade

# Install TeXLive 2018
RUN apt-get -y install software-properties-common \
	&& add-apt-repository ppa:jonathonf/texlive-2018 \
	&& apt-get update
RUN apt-get -y install texlive

# Additional packages required to run TeXLive
RUN apt-get -y install wget xzdec
