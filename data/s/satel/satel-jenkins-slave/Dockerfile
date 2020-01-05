FROM jenkins/jnlp-slave:3.29-1

# Root is required to modify uid
USER root

# Assign jenkins user to the docker group
RUN groupadd -g 995 docker && usermod -a -G docker jenkins

# Install the latest Docker CE binaries
RUN apt-get update\
    && apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common\
    && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey\
    && apt-key add /tmp/dkey\
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"\
    && apt-get update\
    && apt-get -y install docker-ce python3-pip\
    && pip3 install docker-compose\
    && curl -L https://github.com/docker/machine/releases/download/v0.14.0/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine\
    && chmod +x /usr/local/bin/docker-machine

# restore ENTRYPOINT to startup as jenkins user
USER jenkins
