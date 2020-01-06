FROM ubuntu:trusty

RUN apt-get update && \
    apt-get -y install git curl && \
    rm -rf /etc/puppet/puppet.conf && \
    curl -sO https://apt.puppetlabs.com/puppetlabs-release-trusty.deb && \
    dpkg -i puppetlabs-release-trusty.deb && \
    rm puppetlabs-release-trusty.deb && \
    apt-get update && \
    apt-get -y install puppet build-essential ruby-dev && \
    gem install librarian-puppet --no-rdoc --no-ri

ONBUILD COPY Puppetfile /etc/puppet/
ONBUILD COPY hiera.yaml /etc/puppet/
ONBUILD COPY puppet.conf /etc/puppet/
ONBUILD COPY site.pp /etc/puppet/manifests/
ONBUILD COPY common.yaml /var/lib/hiera/

ONBUILD RUN cd /etc/puppet && \
            librarian-puppet install && \
            puppet apply manifests/site.pp
