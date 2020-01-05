FROM jenkins/jenkins:lts
USER root

RUN apt-get update && \
apt-get -y install apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common && \
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable" && \
apt-get update && \
apt-get -y install docker-ce
RUN apt-get install -y docker-ce
RUN usermod -aG docker jenkins
RUN usermod -aG users jenkins
USER jenkins

# Suppress apt installation warnings
ENV DEBIAN_FRONTEND=noninteractive

# Change to root user
USER root

# Install base packages
RUN apt-get update -y && \
    apt-get -y install apt-transport-https curl python-dev python-setuptools make && \
    easy_install pip


# Install Docker Compose
RUN pip install docker-compose && \
    pip install ansible boto boto3

# Change to jenkins user
USER jenkins

# Add Jenkins plugins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt