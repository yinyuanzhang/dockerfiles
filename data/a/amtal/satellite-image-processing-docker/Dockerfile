FROM ubuntu:18.04

ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
ENV OCSSW_HOME=/usr/local/ocssw
ENV OCDATAROOT=$OCSSW_HOME/share

RUN apt-get update
RUN apt-get install -y openjdk-8-jre-headless libgdal-java wget git python
RUN ln -s /usr/lib/jni/* /usr/lib

RUN wget http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64.tar.gz
RUN tar xvzf jai-1_1_3-lib-linux-amd64.tar.gz
RUN cp jai-1_1_3/lib/*.jar $JAVA_HOME/jre/lib/ext && cp jai-1_1_3/lib/*.so $JAVA_HOME/jre/lib/amd64
RUN rm -rf jai-1_1_3-lib-linux-amd64.tar.gz jai-1_1_3

RUN wget http://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz
RUN tar xvzf jai_imageio-1_1-lib-linux-amd64.tar.gz
RUN cp jai_imageio-1_1/lib/*.jar $JAVA_HOME/jre/lib/ext && cp jai_imageio-1_1/lib/*.so $JAVA_HOME/jre/lib/amd64
RUN rm -rf jai_imageio-1_1-lib-linux-amd64.tar.gz jai_imageio-1_1 

RUN wget https://oceandata.sci.gsfc.nasa.gov/ocssw/install_ocssw.py && python install_ocssw.py --install-dir=$OCSSW_HOME --aqua
RUN rm install_ocssw.py

