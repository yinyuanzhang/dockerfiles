FROM ubuntu:18.04

MAINTAINER <christoph.hahn@uni-graz.at>

RUN apt-get update && apt-get -y upgrade && \
        apt-get install -y build-essential wget 

WORKDIR /usr/src

RUN wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz && \
	tar xvfz v8.2.12.tar.gz && \
	cd standard-RAxML-8.2.12 && \
	make -f Makefile.SSE3.PTHREADS.gcc && \
	rm *.o && \
	ln -s $(pwd)/raxmlHPC-PTHREADS-SSE3 /usr/bin/raxml && \
	chmod a+x ./usefulScripts/*.* && \
	sed -i 's/^\$raxmlExecutable =*.*/\$raxmlExecutable = "raxml";/' ./usefulScripts/ProteinModelSelection.pl && \
	ln -s $(pwd)/usefulScripts/*.* /usr/bin/

#ENV PATH="/usr/src/standard-RAxML-8.2.12/usefulScripts:${PATH}"

#create working directory and move to entrypoint
VOLUME /home/data
WORKDIR /home/data

