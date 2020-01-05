FROM jenkinsci/jenkins:2.11

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

ENV ADMIN_USERNAME admin
ENV DEFAULT_ADMIN_PASSWORD control246
ENV ADMIN_PASSWORD $DEFAULT_ADMIN_PASSWORD

COPY init_scripts/*.groovy  /usr/share/jenkins/ref/init.groovy.d/
