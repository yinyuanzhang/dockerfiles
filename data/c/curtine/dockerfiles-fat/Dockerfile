FROM ubuntu:18.04

RUN apt update -y &&\
    DEBIAN_FRONTEND='noninteractive' apt install -y cmake g++ libpoco-dev\
      lsb-release libboost-test-dev perl gpg clang systemd init libssl-dev\
      net-tools vim curl wget &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -c -s)-pgdg main" >> /etc/apt/sources.list.d/pgdg.list &&\
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt update -y &&\
    DEBIAN_FRONTEND='noninteractive' apt install -y postgresql-server-dev-10\
      postgresql-10 &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

