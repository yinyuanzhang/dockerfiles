FROM jenkins/jenkins:lts
LABEL maintainer="colab@strypes.eu"

#Install build dependencoes
#USER root
#RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - && apt-get install -y nodejs

USER jenkins
#Disable the setup wizard
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false ${JAVA_OPTS:-}"

#Copy files to right locations.
COPY groovy/executors.groovy /usr/share/jenkins/ref/init.groovy.d/10_executors.groovy
COPY groovy/security.groovy /usr/share/jenkins/ref/init.groovy.d/20_security.groovy
COPY groovy/sshcredentials.groovy /usr/share/jenkins/ref/init.groovy.d/30_sshcredentials.groovy
COPY groovy/addNodeToJenkins.groovy /usr/share/jenkins/ref/init.groovy.d/40_AddNodeToJenkins.groovy

#Plugins
COPY configuration/plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt