FROM jenkins/jenkins:lts

# add sudo without password, so jenkins can do `sudo docker ...`
USER root
RUN apt-get update && \
apt-get -y install apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common && \
apt-get install -y sudo && \
rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

# back to business
USER jenkins
