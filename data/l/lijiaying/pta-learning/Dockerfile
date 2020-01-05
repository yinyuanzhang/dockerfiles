FROM ubuntu:16.04
MAINTAINER lijiaying <lijiaying1989@gmail.com>

## install essential dependency
RUN apt-get update && \
	apt-get -y --no-install-recommends install \
	g++ m4 \
	ocaml libextlib-ocaml libextlib-ocaml-dev libgmp-ocaml libgmp-ocaml-dev \
	libgmp-dev libppl-dev openmpi-bin openmpi-common libopenmpi-dev oasis \
	graphviz plotutils wget git bzip2 make python \
	cmake libgsl0-dev libz3-dev


# get and set up ppl library
RUN wget http://bugseng.com/products/ppl/download/ftp/releases/1.2/ppl-1.2.tar.bz2 && \
	tar -xjvf ppl-1.2.tar.bz2 && \
	rm -rf ppl-1.2.tar.bz2 && \
	cd ppl-1.2 && \
	./configure --prefix=/usr && \
	cd interfaces/OCaml/ && \
	make && \
	make install

	
# get imitator source and revert to a specific version, after which compile the whole source code
RUN mkdir -p /imitator && \
	cd /imitator && \
	git config --global http.sslVerify false && \
	git clone https://github.com/etienneandre/imitator.git latest && \
	cp -rf latest old


RUN	cd /imitator/latest && \
	cp METAS/* /usr/lib/ocaml/METAS/ && \
	sh build.sh && \
	ln -s /imitator/latest/bin/imitator /bin/imitator-latest


RUN cd /imitator/old && \
	git checkout 2a45bb9 && \
	cp METAS/* /usr/lib/ocaml/METAS/ && \
	sh compile.sh && \
	ln -s /imitator/old/bin/imitator /bin/imitator-old

COPY . /pta-learning

# make a test directory
#RUN mkdir /test && \
#	apt-get install -y vim
