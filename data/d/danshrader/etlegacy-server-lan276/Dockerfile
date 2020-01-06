FROM ubuntu:18.04

ENV ETL_PATH /root/etlegacy

RUN apt-get update -y && apt-get install -y wget
RUN apt-get install -y nano
RUN wget -O etlegacy-v2.76-x86_64.tar.gz https://www.etlegacy.com/download/file/121 \
&& tar -xzf etlegacy-v2.76-x86_64.tar.gz && rm -f etlegacy-v2.76-x86_64.tar.gz \
&& mv etlegacy-v2.76-x86_64 $ETL_PATH

ENV PAK_MIRROR mirror.etlegacy.com/etmain/

WORKDIR $ETL_PATH/etmain
RUN wget http://$PAK_MIRROR/pak0.pk3 \
&& wget http://$PAK_MIRROR/pak1.pk3 \
&& wget http://$PAK_MIRROR/pak2.pk3 \
&& wget http://$PAK_MIRROR/mp_bin.pk3

COPY etl_server.cfg /root/etlegacy/etmain/
EXPOSE 27960/udp
