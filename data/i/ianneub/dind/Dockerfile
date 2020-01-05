FROM ubuntu:14.04
MAINTAINER ian@ianneubert.com

# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables \
    make
    
# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ubuntu/ | sh

# Install Docker compose
RUN curl -L https://github.com/docker/compose/releases/download/1.2.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
CMD ["wrapdocker"]

