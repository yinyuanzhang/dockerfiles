FROM cfplatformeng/tile-generator:v14.0.3

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y curl git ssh jq

RUN pip install --upgrade ruamel.yaml==0.15.85 PyGithub==1.43.4 awscli==1.15.5

RUN wget -O /tmp/pivnet-linux-amd64-0.0.55 https://github.com/pivotal-cf/pivnet-cli/releases/download/v0.0.55/pivnet-linux-amd64-0.0.55
RUN mv /tmp/pivnet-linux-amd64-0.0.55 /usr/local/bin/pivnet
RUN chmod 755 /usr/local/bin/pivnet

RUN apt-get clean

RUN groupadd -g 1031 jenkins
RUN useradd -m -d /home/jenkins -s /bin/bash -u 1030 -g 1031 jenkins
ENV HOME="/home/jenkins"