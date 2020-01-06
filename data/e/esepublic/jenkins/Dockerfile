FROM debian:jessie
MAINTAINER Keith Bentrup <kbentrup@ebay.com>

COPY jenkins-ci.org.key /tmp/

RUN apt-key add /tmp/jenkins-ci.org.key && \
  echo "deb http://pkg.jenkins-ci.org/debian binary/" >> /etc/apt/sources.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
  openjdk-7-jre-headless \
  net-tools \
  python-setuptools \
  jenkins \
  git && \
  apt-get --purge autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

RUN easy_install pip && \
  pip install -U docker-compose

EXPOSE 8080

# COPY jenkins-${JENKINS_VERSION}.war /opt/jenkins-${JENKINS_VERSION}.war
# COPY jenkins ${JENKINS_HOME}

# CMD /usr/bin/java -Djava.awt.headless=true -jar /usr/share/jenkins/jenkins.war --webroot=/var/cache/jenkins/war --httpPort=8080 --ajp13Port=-1
# ENV JENKINS_HOME=/var/lib/jenkins
