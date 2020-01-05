FROM jenkins/jenkins:lts
USER root
# Install 
RUN apt-get update && \
apt-get -y install apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
    
RUN usermod -a -G jenkins jenkins
USER jenkins
