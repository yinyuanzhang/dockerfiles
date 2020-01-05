ARG jenkins_version='2.190.3'
FROM jenkins/jenkins:${jenkins_version}

USER root

# Install plugins
ARG plugins_file='plugins.txt'
COPY ${plugins_file} /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

USER jenkins
