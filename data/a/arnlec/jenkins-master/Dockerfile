FROM jenkins/jenkins:lts

ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false -Djenkins.CLI.disabled=true"
RUN /usr/local/bin/install-plugins.sh kubernetes
USER jenkins
ADD hardening.groovy $JENKINS_HOME/init.groovy.d/hardening.groovy