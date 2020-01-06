FROM plusbyte/dind:latest

MAINTAINER Decheng Zhang <killercentury@gmail.com>

ENV SWARM_CLIENT_VERSION 3.9
ENV DOCKER_COMPOSE_VERSION 1.3.3
ENV RANCHER_CLI_VERSION 0.6.8

# Add a Jenkins user with permission to run docker commands
RUN useradd -r -m -G docker jenkins

# Install necessary packages
RUN apt-get update && apt-get install -y curl zip openjdk-9-jre-headless supervisor git && rm -rf /var/lib/apt/lists/*

# Install Jenkins Swarm Client
RUN wget -q https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}.jar -P /home/jenkins

# Install Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Install Rancher CLI
RUN wget -q https://releases.rancher.com/cli/v${RANCHER_CLI_VERSION}/rancher-linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz -P /tmp
RUN tar -xvzf /tmp/rancher-linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz -C /tmp && mv /tmp/rancher-v${RANCHER_CLI_VERSION}/rancher /usr/local/bin/rancher && rm -r /tmp/rancher-*

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
