FROM ubuntu:14.04
MAINTAINER Robby Lee <robby.libb@sslab.cs.nthu.edu.tw>

# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables
    
# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ubuntu/ | sh
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

# Install ssh and apache
RUN apt-get purge -y openssh-client
RUN apt-get install -y openssh-server apache2 supervisor openssh-server ssh-import-id
RUN apt-get install -y nano
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor

RUN useradd -r -g docker robby
RUN mkdir -p /home/robby/hw3/dind
COPY Dockerfile supervisord.conf wrapdocker /home/robby/hw3/dind/
# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
VOLUME /var/lib/docker
CMD ["wrapdocker"]

# Use supervisord to manage ssh and apache
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 22 80 5080 5180 5280 5380
CMD ["/usr/bin/supervisord"]

WORKDIR /home/robby/hw3/dind/
