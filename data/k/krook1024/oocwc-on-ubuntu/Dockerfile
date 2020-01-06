FROM dorowu/ubuntu-desktop-lxde-vnc:bionic

# OOCWC files
ADD justine/ /root/Desktop/justine/
ADD debrecen.osm /root/Desktop/justine/
ADD run.sh /root/Desktop/

# dependencies
RUN apt update \
    && apt install -y libtool m4 automake autoconf libosmium-dev\
    g++ curl make libboost-all-dev pkg-config protobuf-compiler libprotobuf-dev \
    flex libgflags-dev libosmpbf-dev maven openjdk-8-jdk openjdk-8-jre telnet

# compile OOCWC/rcemu
RUN cd /root/Desktop/justine/rcemu \
    ; autoreconf --install \
    ; ./configure \
    ; make


# compile OOCWC/rclog
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
RUN update-alternatives --set javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac
RUN java -version
RUN cd /root/Desktop/justine/rclog \
    ; mvn clean compile package site assembly:assembly
