FROM maosmurf/oracle-jdk

MAINTAINER Adam Zielinski <adam@maosmurf.com>

RUN wget --no-verbose -O /tmp/apache-maven-3.tar.gz \
    http://www.eu.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz
RUN wget --no-verbose -O /tmp/apache-maven-3.tar.gz.md5 \
    http://www.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz.md5

# verify checksum
RUN echo "`cat /tmp/apache-maven-3.tar.gz.md5` /tmp/apache-maven-3.tar.gz" | md5sum -c

# install
RUN tar xzf /tmp/apache-maven-3.tar.gz -C /opt/
RUN mv /opt/apache-maven-3* /opt/apache-maven-3
RUN ln -s /opt/apache-maven-3/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-3.tar.gz{,.md5}

ENV M2_HOME /opt/apache-maven-3
