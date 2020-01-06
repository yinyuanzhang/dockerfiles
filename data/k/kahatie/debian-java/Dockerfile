FROM kahatie/debian:jessie
MAINTAINER kahatie <kahatie@gmail.com>

# Mise a jour / installation des packet
RUN apt-get update && apt-get install -y\
 openjdk-7-jre\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*
 
