FROM jenkins/jenkins:2.170-alpine

# Set the directory config as code plugin will search
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc

# Disable setup wizard
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Add list of plugins to install at build time
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

# Add script creating admin user at startup, requires docker secrets
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy

# Create configuration as code directory
COPY --chown=jenkins:jenkins casc_configs /var/jenkins_home/casc

# Install plugins
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt


