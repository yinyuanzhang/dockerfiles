 
FROM java:7

MAINTAINER Larry Liang <ptolemy428@gmail.com>

ENV MAVEN_VERSION 3.2.5

#maven
RUN curl -sSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
     && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
     && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
ENV MAVEN_HOME /usr/share/maven
ENV M2_HOME /usr/share/maven

#phantomjs
RUN apt-get update \
    && apt-get install -y bzip2 \
    && apt-get install -y less \
    && apt-get install -y vim \
    && apt-get install -y curl
    
RUN cd /tmp
RUN curl -sSL https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2 | tar -xj -C /usr/local/share/ \
    && ln -s /usr/local/share/phantomjs-1.9.8-linux-x86_64 /usr/local/share/phantomjs \
    && ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs

WORKDIR /root/dev


