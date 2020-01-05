#Base docker contanier for SAMP server with x86 support
#FROM debian:latest
FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
#installing apt utils
RUN apt-get install -y apt-utils
RUN apt-get update -y

RUN dpkg --add-architecture i386

RUN apt-get update -y

RUN apt-get install libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386 lib32stdc++6 -y

RUN apt-get install zip bash tar unzip screen wget -y

RUN  apt-get update -y

#############INSTALL JAVA RUNTIME################
#RUN apt-get install default-jre:i386 -y

###JAVA 8 i386 installation
##Additional repository installation
RUN apt-get install software-properties-common -y
RUN apt-get update
RUN add-apt-repository ppa:openjdk-r/ppa -y
RUN apt-get update
##JAVA 8 JRE installation
RUN apt-get install openjdk-8-jdk:i386 -y
RUN apt-get update
RUN update-alternatives --install /usr/bin/java java  /usr/lib/jvm/java-1.8.0-openjdk-i386/jre/bin/java 2000

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-i386
ENV LD_LIBRARY_PATH=.:/usr/lib/jvm/java-1.8.0-openjdk-i386/jre/lib/i386:/usr/lib/jvm/java-1.8.0-openjdk-i386/jre/lib/i386/client:/usr/lib/jvm/java-1.8.0-openjdk-i386/jre/lib/i386/server:/usr/local/lib

#update
RUN apt-get update && apt-get upgrade -y

#CMD ["/bin/bash"]





