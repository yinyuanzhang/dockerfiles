FROM fgodinho/hlf-peer 
# use locally compiled peer
# install java and ant
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer ant
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/
# setup juds, prerequisite for hlf bftsmart
RUN apt-get install -y libc6-dev-i386 autoconf
COPY juds.tar.gz /
RUN tar -xzvf juds.tar.gz
RUN apt-get install --reinstall make
RUN cd juds && ./autoconf.sh && ./configure && make && make install
RUN rm -rf juds
# deploy xsp java module
COPY hlf-xsp.jar /
COPY runXSP.sh /
COPY startPeer.sh /
