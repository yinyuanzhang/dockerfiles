FROM centos:centos7
MAINTAINER pcman312 <pcman312@gmail.com>

WORKDIR /tmp/

RUN yum install -y wget which rsync git openssh-clients java

# Install Rundeck CLI
RUN wget https://bintray.com/rundeck/rundeck-rpm/rpm -O bintray.repo
RUN mv bintray.repo /etc/yum.repos.d/
RUN yum install -y rundeck-cli

# Install jq
RUN wget http://stedolan.github.io/jq/download/linux64/jq
RUN chmod +x ./jq
RUN mv ./jq /usr/bin

# Set up .ssh folders
RUN mkdir -p /root/.ssh/sockets
