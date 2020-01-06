FROM ubuntu:18.04

MAINTAINER <christoph.hahn@uni-graz.at>

RUN apt-get update && apt-get -y upgrade && \
        apt-get install -y build-essential vim git wget python \
	autoconf automake gcc libtool \
	yaggo fig2dev gnuplot xfig
#        python3 python3-pip 
#        exonerate hmmer ncbi-blast+

WORKDIR /usr/src

RUN git clone --recursive https://github.com/jgurtowski/ectools.git && \
	cd ectools && \
	git reset --soft 031eb0300c82392915d8393a5fedb4d3452b15bf && \
	cd ..

RUN wget https://github.com/mummer4/mummer/archive/v4.0.0beta2.tar.gz && \
	tar xvfz v4.0.0beta2.tar.gz && \
	cd mummer-4.0.0beta2/ && \
	autoreconf -fi && \
	./configure --prefix=/usr/bin && \
	make && make install && \
	cd .. && rm v4.0.0beta2.tar.gz

ENV PATH="/usr/src/mummer-4.0.0beta2:${PATH}"

RUN chmod a+x /usr/src/ectools/*[a-z].py && \
	ln -s /usr/src/ectools/*[a-z].py /usr/bin/


#create working directory and move to entrypoint
VOLUME /home/data
WORKDIR /home/data

