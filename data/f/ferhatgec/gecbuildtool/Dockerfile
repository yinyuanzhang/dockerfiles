FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y yasm genext2fs build-essential wget libmpfr-dev libmpc-dev libgmp3-dev qemu autoconf automake texinfo pkg-config git ctags gperf && \
    apt-get install -y locales && \
    apt-get install -y grub-pc-bin xorriso

ADD build/   /opt/build

RUN locale-gen "tr_TR.UTF-8"

RUN chmod -R 777 /opt/build/python.sh
RUN chmod -R 777 /opt/build/git.sh
RUN chmod -R 777 /opt/build/build.sh
