FROM debian:latest

RUN apt-get update && \
  	apt-get install -y openssh-client && \
  	rm -rf /var/lib/apt/lists/* && \
  	apt-get clean
