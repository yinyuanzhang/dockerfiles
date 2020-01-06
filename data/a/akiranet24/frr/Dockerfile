FROM ubuntu:bionic

WORKDIR /root
ENV FRRVER frr-stable

RUN apt update \
 && apt install -y unzip curl wget git vim iproute2 iputils-ping net-tools

RUN apt install -y gnupg tcpdump traceroute ca-certificates build-essential

RUN curl -s https://deb.frrouting.org/frr/keys.asc | apt-key add - \
 && echo deb https://deb.frrouting.org/frr bionic $FRRVER | tee -a /etc/apt/sources.list.d/frr.list \
 && apt update \
 && apt install frr frr-pythontools -y

