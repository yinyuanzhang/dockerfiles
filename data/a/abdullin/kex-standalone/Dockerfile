FROM archlinux/base:latest
MAINTAINER Azat Abdullin <abdullin@kspt.icc.spbstu.ru>

ENV Z3_VERSION "4.7.1"
ENV JAVA_HOME /lib/jvm/default

WORKDIR /home
COPY . /home
RUN ./configure.sh && ./build.sh
