FROM jenkins:2.7.2

COPY plugins.txt /usr/share/jenkins/ref/
#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/ref/plugins.txt | tr '\n' ' ')