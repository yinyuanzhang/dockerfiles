FROM ubuntu:16.04
LABEL maintainer jan.szumiec@gmail.com
RUN apt update && apt upgrade -y &&\
    apt install -y software-properties-common &&\
    add-apt-repository --yes ppa:js-reynaud/kicad-5 &&\
    apt update &&\
    apt install -y xserver-xorg-video-dummy kicad gerbv make &&\
    rm -rf /var/lib/apt/list/* 

COPY scripts /scripts

VOLUME /workdir

WORKDIR /workdir

#ENTRYPOINT ["/scripts/plot_board.py"]