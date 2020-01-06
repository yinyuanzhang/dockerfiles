FROM ubuntu:16.04

LABEL maintainer="me@lehungio.com"

# env
USER root
WORKDIR /code

# dependencies
RUN apt-get update
RUN apt-get -y install wget

# run sudo
RUN apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update

# install java bin
# Manual download - Java SE Development Kit
# http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html
# split -b 90MB jdk-10.0.1_linux-x64_bin.tar.gz "JDK-10.0.1"

RUN mkdir /opt/java-jdk
COPY ./src/JDK-10.0.1* /opt/java-jdk/
RUN cat /opt/java-jdk/JDK* > /opt/java-jdk/jdk-10.0.1_linux-x64_bin.tar.gz
RUN sudo tar -C /opt/java-jdk -xzvf /opt/java-jdk/*.tar.gz
RUN sudo update-alternatives --install /usr/bin/java java /opt/java-jdk/jdk-10.0.1/bin/java 1
RUN sudo update-alternatives --install /usr/bin/javac javac /opt/java-jdk/jdk-10.0.1/bin/javac 1
RUN java --version
RUN javac --version

# ENTRYPOINT ["top", "-b"]
# CMD ["-c"]
# ENTRYPOINT ["/bin/bash"]