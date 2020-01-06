FROM jenkins/jenkins:lts-alpine

USER root
COPY plugins.txt /usr/share/jenkins/ref/plugins/plugins.txt
COPY /configs/users "$JENKINS_HOME"/users/
COPY /configs/locale.xml "$JENKINS_HOME"/locale.xml
COPY /configs/jenkins_home_config.xml "$JENKINS_HOME"/config.xml
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins/plugins.txt
USER jenkins
