FROM jenkins:latest

MAINTAINER Aboubakar Koïta "aboubakar.koita@yahoo.fr"

USER root
RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install -y git
ADD plugins.txt /usr/share/jenkins/ref/
RUN chmod 777 /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt


RUN curl -sSL http://archive.apache.org/dist/maven/maven-3/3.3.3/binaries/apache-maven-3.3.3-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-3.3.3 /usr/share/maven \
  && rm -rf /usr/bin/mvn \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
  
ENV MAVEN_HOME /usr/share/maven

ADD ./settings.xml $MAVEN_HOME/conf/

#ADD jenkins.sh /usr/local/bin/jenkins.sh

RUN groupadd -g 999 vboxsf

RUN gpasswd -a jenkins vboxsf 

RUN gpasswd -a jenkins root

USER jenkins

RUN chmod 777 -R "$JENKINS_HOME"

USER root
