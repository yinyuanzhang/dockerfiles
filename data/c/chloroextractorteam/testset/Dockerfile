FROM ubuntu:xenial

LABEL maintainer="foersterfrank@gmx.de"

RUN apt update && apt install --yes sra-toolkit wget

RUN mkdir /script
ADD download_sra_and_extract.sh /script

VOLUME /data

CMD /script/download_sra_and_extract.sh
