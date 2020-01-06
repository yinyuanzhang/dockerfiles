FROM ubuntu:15.04
RUN apt-get update
RUN apt-get install -y git python curl wget parallel build-essential automake m4 perl autotools-dev texinfo linux-libc-dev libmpfr4 libmpc-dev cmake
 
RUN git clone https://github.com/chunkeey/carl9170fw.git
RUN cd carl9170fw ; \
    make -C toolchain