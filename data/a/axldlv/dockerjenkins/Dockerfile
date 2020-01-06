FROM jenkins/jenkins:2.91

MAINTAINER AxelDlv

# use Root user
USER root

# Prerequisites for docker
RUN apt-get update \
    && apt-get -y install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common


# Docker repos
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
   stable" 

# Update Cache and search docker-ce
RUN apt-get update
RUN apt-cache search docker-ce

# docker
RUN apt-get -y install docker-ce

# give jenkins docker rights
RUN usermod -aG docker jenkins

# Use Jenkins user
USER jenkins

# Expose on 49001 (local) from 8080 (Jenkins)
EXPOSE 49001
