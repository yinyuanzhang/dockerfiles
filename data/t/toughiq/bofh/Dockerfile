FROM ubuntu:18.04
MAINTAINER toughIQ<toughiq@gmail.com>

RUN apt-get update && apt-get install -y fortunes-bofh-excuses \
    && apt-get clean all && rm -rf /var/lib/apt/lists/*
    
CMD ["/usr/games/fortune"]
