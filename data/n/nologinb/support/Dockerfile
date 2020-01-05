FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
  wget \
  net-tools \
  mc \
  iputils-ping \
  dnsutils \
  iperf \
  python3 \
  python3-pip \
  curl \
  telnet \
  groff \
  vim \
  less \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install awscli awslogs boto3 rvs-awsume requests

RUN awsume --install-plugin https://raw.githubusercontent.com/vetaljanos/awsume/master/examplePlugin/console.py https://raw.githubusercontent.com/vetaljanos/awsume/master/examplePlugin/console.yapsy-plugin

RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest \
  && chmod +x /usr/local/bin/ecs-cli
