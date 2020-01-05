FROM ubuntu

RUN apt update
RUN apt upgrade --assume-yes
RUN apt install --assume-yes git
RUN git clone --branch 2.7.2 https://github.com/ndierckx/NOVOPlasty
RUN ln -s /NOVOPlasty/NOVOPlasty2.7.2.pl /NOVOPlasty/NOVOPlasty.pl
VOLUME /data
WORKDIR /data
