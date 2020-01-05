FROM ubuntu:latest

MAINTAINER Jens Dede <mail@jdede.de>

# Install prerequisites
RUN apt-get update && apt-get install -y git maven default-jdk

RUN mkdir -p /root/src/

# Get Californium
WORKDIR /root/src
RUN git clone https://github.com/mkovatsc/Californium.git
WORKDIR /root/src/Californium

# Building is not necessary: Binaries are in the repository.
#RUN mvn clean install

WORKDIR /root
ADD tools /root
RUN chmod +x start_coap

EXPOSE 5683

CMD ["/root/start_coap"]
