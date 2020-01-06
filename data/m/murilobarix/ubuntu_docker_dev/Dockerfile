
FROM ubuntu:16.04
ARG CACHEBUST=1
RUN dpkg --add-architecture i386 
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libboost-all-dev openocd default-jre default-jdk  meld kate mc minicom build-essential git zlib1g-dev libncurses-dev libssl-dev gawk unzip wget python subversion openssl file cmake doxygen mscgen graphviz plantuml wine curl ccache gettext tcl-dev tk-dev python-setuptools python-pip clang-format sshpass 
RUN pip install cpplint

 
