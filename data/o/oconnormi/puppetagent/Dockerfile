FROM ubuntu:xenial
MAINTAINER oconnormi

RUN apt-get update && apt-get install -y wget && \
    wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb && \
    dpkg -i puppetlabs-release-pc1-xenial.deb && \
    rm -rf puppetlabs-release-pc1-xenial.deb && \
    apt-get update && apt-get install -y puppet-agent

EXPOSE 8140

ENTRYPOINT ["/bin/bash", "-c", "/opt/puppetlabs/bin/puppet agent --verbose --no-daemonize"]
