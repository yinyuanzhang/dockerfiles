FROM ubuntu:16.04
MAINTAINER Songtao Mai <songtao.mai@gmail.com>
RUN apt-get update && \
    apt-get install curl git sudo -y && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g shadowsocks-manager-kesuki
ENTRYPOINT ["/usr/bin/ssmgr"]
