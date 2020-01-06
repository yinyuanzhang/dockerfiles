FROM ubuntu:16.04
MAINTAINER Pallam <Darkmasters@yandex.ru>
# Modified by pallam
RUN  date +%T:%N
# Install core dependencies

RUN apt-get update && apt-get -y install \
    autoconf automake autopoint bash bison bzip2 flex g++ \
    g++-multilib gettext git gperf intltool libc6-dev-i386 \
    libgdk-pixbuf2.0-dev libltdl-dev libssl-dev libtool-bin \
    libxml-parser-perl make openssl p7zip-full patch perl pkg-config \
    python ruby sed unzip wget xz-utils g++-multilib libc6-dev-i386

RUN apt-get -y install curl

# Choose Qt version

ENV QT_VERSION_MAJOR 5.9
ENV QT_VERSION 5.9.4

# Compile and install Qt Base

ENV QT_DIST /usr/local/Qt-"$QT_VERSION"
ENV QT_BASE_SRC https://download.qt.io/official_releases/qt/"$QT_VERSION_MAJOR"/"$QT_VERSION"/single/qt-everywhere-opensource-src-"$QT_VERSION".tar.xz
ENV QT_BASE_DIR /qtbase-opensource-src-"$QT_VERSION"

RUN curl -sSL $QT_BASE_SRC | tar xJ \
    && cd $QT_BASE_DIR \
    && bash ./configure -opensource -confirm-license -static -no-qml-debug \
       -openssl-linked -qt-pcre -qt-zlib -qt-pcre -qt-libpng -qt-libjpeg -qt-freetype   \
       -no-compile-examples -nomake examples -nomake tests -nomake tools \
       -platform linux-g++-64 \
    && make install

ENV PATH $QT_DIST/bin:$PATH

RUN cd /root && git clone https://github.com/mxe/mxe.git
RUN cd /root/mxe && make qt5
