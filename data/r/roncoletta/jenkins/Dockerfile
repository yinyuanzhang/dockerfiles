FROM roncoletta/maven
MAINTAINER Wagner Roncoletta <wagner.roncoletta@gmail.com>

RUN echo " deb http://pkg.jenkins-ci.org/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list

RUN apt-get update && \
  # SVN Client
  apt-get install -y curl libsvn-perl subversion \
  # Git Client
  git


RUN apt-get install -y --force-yes jenkins && \
             apt-get autoremove -y && \
             apt-get clean


ENV JENKINS_HOME /var/lib/jenkins
RUN mkdir -p $JENKINS_HOME/init.groovy.d

EXPOSE 8080

VOLUME /var/lib/jenkins

#Copy others JDK

ENV JAVA_6 /opt/java/jdk6
ENV JAVA_8 /opt/java/jdk8

RUN mkdir -p $JAVA_6
RUN mkdir -p $JAVA_8

VOLUME $JAVA_6
VOLUME $JAVA_8

RUN chown -hR jenkins:jenkins $JENKINS_HOME

ADD HOOK.groovy $JENKINS_HOME/init.groovy.d

ADD jenkins.sv.conf /etc/supervisor/conf.d/
CMD supervisord -c /etc/supervisor.conf

