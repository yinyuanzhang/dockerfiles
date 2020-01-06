FROM    centos
LABEL      maintainer="Xiayu.Li"

RUN yum install wget -y
RUN yum install unzip -y

WORKDIR /home
RUN wget https://dl.google.com/android/repository/android-ndk-r18b-linux-x86_64.zip
RUN unzip android-ndk-r18b-linux-x86_64.zip
RUN rm android-ndk-r18b-linux-x86_64.zip
