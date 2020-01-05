FROM jenkins:1.642.1

USER root
RUN userdel jenkins
RUN useradd -d /var/jenkins_home -u 9998 jenkins
RUN chown -R jenkins:jenkins /var/jenkins_home

USER jenkins
