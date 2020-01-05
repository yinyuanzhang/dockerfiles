FROM jenkins/jenkins:alpine

COPY plugins /tmp/plugins
RUN /tmp/plugins/create-plugins-list.sh
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

USER jenkins
