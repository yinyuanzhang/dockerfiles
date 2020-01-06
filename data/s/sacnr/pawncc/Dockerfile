FROM i386/debian:buster-slim

RUN apt-get update && apt-get upgrade
RUN apt-get install -y wget
RUN wget https://github.com/pawn-lang/compiler/releases/download/v3.10.9/pawnc-3.10.9-linux.tar.gz -O /pawnc.tar.gz
RUN mkdir /pawnc
RUN tar -vxzf /pawnc.tar.gz -C /pawnc && mv /pawnc/pawnc*/* /pawnc
RUN cp /pawnc/lib/libpawnc.so /usr/local/lib
RUN ldconfig
RUN cp /pawnc/bin/pawn* /usr/local/bin
RUN mkdir /samp

WORKDIR "/samp"
CMD ["/bin/bash"]
