FROM ubuntu:18.04

RUN dpkg --add-architecture i386

RUN apt-get update

RUN apt-get install -y curl unzip

RUN curl 'https://dl.google.com/dl/android/studio/ide-zips/3.2.1.0/android-studio-ide-181.5056338-linux.zip' > /tmp/studio.zip && unzip -d /opt /tmp/studio.zip && rm /tmp/studio.zip

RUN apt-get install -y xorg

RUN apt-get install -y vim ant

RUN apt-get install -y openjdk-8-jre openjdk-8-jdk

RUN apt-get install -y libz1 libncurses5 libbz2-1.0:i386 libstdc++6 libbz2-1.0 lib32stdc++6 lib32z1 usbutils

RUN apt-get clean

RUN apt-get purge
