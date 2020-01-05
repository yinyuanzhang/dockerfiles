FROM jenkins/jenkins:latest
 
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
ENV PASS=changeme
 
COPY jenkins.sh /usr/share/jenkins/jenkins.sh
USER root
RUN chmod 0755 /usr/share/jenkins/jenkins.sh

RUN apt-get update \
      && apt-get install -y sudo \
      && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && wget -O docker.tgz https://download.docker.com/linux/static/stable/x86_64/docker-17.03.0-ce.tgz \
    && tar -xvf docker.tgz \
    && cp -f docker/* /usr/bin/ \
    && groupadd docker \
    && usermod -G docker jenkins \
    && echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
ENTRYPOINT ["/sbin/tini", "--", "/usr/share/jenkins/jenkins.sh"]

