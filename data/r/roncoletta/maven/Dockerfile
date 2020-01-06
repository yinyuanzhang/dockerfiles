FROM roncoletta/java7
MAINTAINER Wagner Roncoletta <wagner.roncoletta@gmail.com>


ENV MAVEN_VERSION 3.3.9

# download
RUN wget -O /tmp/$MAVEN_VERSION http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz

#Configurations
RUN mkdir -p /usr/share/maven

RUN ls -l

RUN tar -zxf /tmp/$MAVEN_VERSION -C /usr/share/maven

RUN ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

VOLUME /root/.m2

