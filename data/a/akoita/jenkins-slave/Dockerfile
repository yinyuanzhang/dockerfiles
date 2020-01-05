FROM ubuntu:latest

MAINTAINER Aboubakar Koïta "aboubakar.koita@yahoo.fr"

RUN apt-get update

RUN apt-get install -y software-properties-common

RUN add-apt-repository -y ppa:webupd8team/java

RUN apt-get install -y sudo

#ADD ./mysudoers /etc/sudoers.d/
#RUN chmod 0440 /etc/sudoers.d/*
#RUN useradd build --groups root,adm
#USER build

ENV MY_HOME=/root

RUN apt-get install -y aptitude

RUN apt-get install  -y less

RUN apt-get update

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get install  -y oracle-java8-installer

RUN apt-get install  -y oracle-java8-set-default

ENV JAVA_MY_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get install  -y  gdebi

RUN apt-get install -y curl

RUN curl -sL https://deb.nodesource.com/setup | bash -

RUN apt-get install -y nodejs

RUN npm install -g yo bower grunt-cli gulp

RUN mkdir $MY_HOME/jenkins/

ADD ./jenkins-cli.jar $MY_HOME/jenkins/

RUN mkdir $MY_HOME/.ssh

ADD ./id_rsa.pub $MY_HOME/.ssh/

ADD ./id_rsa $MY_HOME/.ssh/

WORKDIR $MY_HOME/.ssh/

RUN pwd 

RUN chmod 777 *

RUN ls -la 

ENV JENKINS_SLAVE_HOME $MY_HOME/jenkins/slave

WORKDIR $MY_HOME/jenkins/

RUN pwd

RUN chmod 777 *.*

RUN ls -la jenkins-cli.jar

RUN apt-get install -y net-tools

EXPOSE 10085

EXPOSE 10086

EXPOSE 10087

RUN apt-get install -y git

RUN curl -sSL http://archive.apache.org/dist/maven/maven-3/3.2.3/binaries/apache-maven-3.2.3-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-3.2.3 /usr/share/maven \
  && rm -rf /usr/bin/mvn \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
  
ENV MAVEN_HOME /usr/share/maven

ADD ./settings.xml $MAVEN_HOME/conf/

#RUN java -jar jenkins-cli.jar -s https://akoita.ci.cloudbees.com/  -i $MY_HOME/.ssh/jenkins_rsa on-premise-executor -fsroot $JENKINS_SLAVE_MY_HOME -name booba-vm -install $MY_HOME/.ssh/jenkins_rsa

RUN npm -g install npm@2.9.0

ADD /.bowerrc $MY_HOME/

ADD ./slave.sh $MY_HOME/jenkins/

ADD ./swarm-client-2.0-jar-with-dependencies.jar $MY_HOME/jenkins/

#RUN chmod 777 $MY_HOME/jenkins/swarm-client-2.0-jar-with-dependencies.jar
ENTRYPOINT  java -jar $MY_HOME/jenkins/swarm-client-2.0-jar-with-dependencies.jar -master http://jenkins-master-service:8080 -name docker-jenkins-node  -disableClientsUniqueId

VOLUME /var/jenkins_slave_maven_repo

VOLUME /root/jenkins/workspace

ADD ./settings.xml $MAVEN_HOME/conf/

ENV TERM=xterm

ENV LANG=en_US.UTF-8

RUN echo 'export LANG=en_US.UTF-8' >> /etc/default/locale