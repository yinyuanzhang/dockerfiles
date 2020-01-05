FROM gcc 

USER root

RUN apt-get update &&\ 
  apt-get install -yq --no-install-recommends apt-utils git gcc clang autoconf automake libtool

RUN git clone https://github.com/json-c/json-c.git
RUN cd json-c && sh autogen.sh && ./configure && make && make install  

COPY test2.c ./test2.c

RUN gcc test2.c -I/usr/local/include -I/usr/local/include/json-c -ljson-c 
ENV LD_LIBRARY_PATH /usr/local/lib

#FROM alpine:3.8

ADD https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

# Define your binary here
ENV fprocess="./a.out"

CMD ["fwatchdog"]


