#Buildmachine for ShoebillPlugin compilation
#by the recommendation of the 
FROM i386/debian

#update
RUN apt-get update
#installing apt utils
RUN apt-get install -y apt-utils
#update
RUN apt-get update
#INSTALL JAVA RUNTIME
RUN apt-get install -y default-jre
#INSTALL JAVA DK
RUN apt-get install -y default-jdk
#update
RUN apt-get update
#INSTALL build essentials including g++ which is C++ compiler on Linux
RUN apt-get install -y build-essential
#INSTALL cmake
RUN apt-get install -y cmake
#install git
RUN apt-get install -y git
#update
RUN apt-get update
#Install libc6
RUN apt-get install libc6-dev
#*****Installing required verion of libiconv*****
RUN apt-get -y install wget
RUN wget https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.15.tar.gz
RUN tar zxf libiconv-1.15.tar.gz
WORKDIR /libiconv-1.15
RUN ./configure --prefix=/usr/local
RUN make
RUN make install
#*****Installing required verion of libiconv*****

RUN apt-get update
RUN ldconfig
RUN iconv --version