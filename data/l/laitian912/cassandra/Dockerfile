FROM cassandra:2.1.12
MAINTAINER Tian Lai <laitian912@gmail.com>

RUN apt-get update
RUN apt-get -y install sudo curl ssh openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd
# Install datastax agent
RUN echo "deb http://debian.datastax.com/community stable main" | tee -a /etc/apt/sources.list.d/datastax.community.list
RUN curl -Lk https://debian.datastax.com/debian/repo_key | apt-key add -
RUN apt-get update
RUN apt-get install datastax-agent

RUN echo "stomp_interface: 172.17.0.2" | sudo tee -a /var/lib/datastax-agent/conf/address.yaml

EXPOSE 22
