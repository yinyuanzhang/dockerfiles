FROM ubuntu:latest

RUN apt-get update \
 && apt-get install -y wget git curl zip make subversion ruby-full openjdk-7-jdk maven \
 && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs
RUN gem install sass compass
RUN npm install -g gulp

ENV JENKINS_VERSION 1.592
RUN mkdir /usr/share/jenkins/
RUN useradd -d /home/jenkins -m -s /bin/bash jenkins

ADD batch-install-jenkins-plugins.sh /usr/local/bin/batch-install-jenkins-plugins.sh
ADD okplugins.list /tmp/okplugins.list
ADD init.groovy /tmp/WEB-INF/init.groovy.d/tcp-slave-angent-port.groovy

# Downloading custom plugins and jenkins. Putting custom plugins into jenkins.war
RUN mkdir -p /tmp/WEB-INF/plugins \
 && batch-install-jenkins-plugins.sh -p /tmp/okplugins.list -d /tmp/WEB-INF/plugins \
 && curl -L http://updates.jenkins-ci.org/download/war/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \
 && cd /tmp \
 && zip -g /usr/share/jenkins/jenkins.war WEB-INF/*/* \
 && rm -rf /tmp/WEB-INF

ENV JENKINS_HOME /var/jenkins_home
RUN usermod -m -d "$JENKINS_HOME" jenkins && chown -R jenkins "$JENKINS_HOME"
VOLUME /var/jenkins_home

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

ADD jenkins.sh /usr/local/bin/jenkins.sh

ENTRYPOINT ["/usr/local/bin/jenkins.sh"]

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

USER jenkins 
