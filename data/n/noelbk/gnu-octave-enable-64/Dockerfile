FROM ubuntu:16.04

WORKDIR /app/octave

RUN apt-get update
RUN apt-get -y install wget unzip curl build-essential cmake git autoconf flex bison
RUN apt-get -y build-dep octave

ADD . .
RUN make -j2 INSTALL_DIR=/usr

# KLUDGE - octave-io fails if it can't find pg_config
RUN ln -s /bin/true /bin/pg_config
RUN octave --eval "pkg update; pkg install -verbose -forge control io signal"
RUN rm /bin/pg_config

CMD octave

