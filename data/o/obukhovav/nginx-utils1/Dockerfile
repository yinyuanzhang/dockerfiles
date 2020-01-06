FROM       nginx:latest
MAINTAINER ObukhovAV "https://github.com/ObukhovAV"
RUN apt-get update
RUN apt-get install -y mc
RUN apt-get install -y nano
RUN apt-get install -y iputils-ping
RUN apt-get install -y curl
RUN apt-get install -y net-tools
RUN apt-get install -y telnet
RUN apt-get install -y dnsutils 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
