FROM ubuntu:16.04
MAINTAINER Korolev A S <gimguo@gmail.com>

WORKDIR /root

RUN apt update
RUN apt-get install -y wget
RUN wget https://github.com/dogecoin/dogecoin/releases/download/v1.14-beta-1/dogecoin-1.14.2-x86_64-linux-gnu.tar.gz
RUN tar -zvxf dogecoin-1.14.2-x86_64-linux-gnu.tar.gz
RUN mv dogecoin-1.14.2 dogecoin
RUN cp dogecoin/bin/* /usr/local/bin

VOLUME ["/opt/dogecoin"]

EXPOSE  8332 18332 22556 44556

CMD ["dogecoind", "--conf=/opt/dogecoin/dogecoin.conf", "--printtoconsole"]