FROM ubuntu
USER root

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y upgrade && apt-get install -y \
	autoconf \
        automake \
        bwa\
        make \
        maven\
        g++ \
        gcc \
        build-essential \
        zlib1g-dev \
        libgsl0-dev \
        curl \
        git \
        wget \
	 r-base-core \
	 software-properties-common
	
RUN add-apt-repository ppa:webupd8team/java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment

WORKDIR /opt
RUN wget https://github.com/PapenfussLab/gridss/releases/download/v2.0.1/gridss-2.0.1-gridss-jar-with-dependencies.jar
RUN mv gridss-2.0.1-gridss-jar-with-dependencies.jar gridss.jar
