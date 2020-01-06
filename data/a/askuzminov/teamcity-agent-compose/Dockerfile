FROM jetbrains/teamcity-agent:latest

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - 

RUN apt-get update

RUN apt-get install -y\
    nodejs\
    docker-ce\
    binutils-gold \
    curl \
    g++ \
    gcc \
    gnupg \
    make \
    python\
    bzip2

RUN curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

RUN curl -L https://releases.rancher.com/cli/v0.6.12/rancher-linux-amd64-v0.6.12.tar.gz -o /tmp/rancher.tar.gz
RUN tar -xzf /tmp/rancher.tar.gz -C /tmp
RUN cp /tmp/rancher-v0.6.12/rancher /usr/local/bin/rancher
RUN chmod +x /usr/local/bin/rancher
RUN rm -rf /tmp/rancher-v0.6.12
RUN rm /tmp/rancher.tar.gz

RUN curl -L https://releases.rancher.com/compose/v0.12.5/rancher-compose-linux-amd64-v0.12.5.tar.gz -o /tmp/rancher-compose.tar.gz
RUN tar -xzf /tmp/rancher-compose.tar.gz -C /tmp
RUN cp /tmp/rancher-compose-v0.12.5/rancher-compose /usr/local/bin/rancher-compose
RUN chmod +x /usr/local/bin/rancher-compose
RUN rm -rf /tmp/rancher-compose-v0.12.5
RUN rm /tmp/rancher-compose.tar.gz
