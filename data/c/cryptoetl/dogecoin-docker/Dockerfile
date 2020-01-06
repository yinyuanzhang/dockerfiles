FROM ubuntu
LABEL maintainer="Allen Day allenday@allenday.com"
RUN apt-get update && apt-get install -y software-properties-common build-essential wget pkg-config 
RUN apt-get install -y libboost-all-dev libssl-dev libevent-dev
RUN apt-get install -y bsdmainutils automake autoconf
WORKDIR /opt
RUN wget https://github.com/dogecoin/dogecoin/releases/download/v1.14-beta-1/dogecoin-1.14.2-x86_64-linux-gnu.tar.gz
RUN tar -xvzf dogecoin-1.14.2-x86_64-linux-gnu.tar.gz
WORKDIR /opt/dogecoin-1.14.2
