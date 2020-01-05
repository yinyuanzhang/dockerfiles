FROM jenkins/jenkins:lts
# Change to root user to install required packages
USER root
RUN apt-get update && apt-get install

# We are hardcoding the groupID here to match the one in the container machine.
# If this needs to be parameterized we should pass it as a build argument
RUN groupadd -g 3000 docker

# Install Docker from official repo
RUN apt-get update -qq && \
    apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update -qq && \
    apt-get install -qqy docker-ce && \
    usermod -aG docker jenkins

# Change to the jenkins user for jenkins-specific modifications
USER jenkins
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
