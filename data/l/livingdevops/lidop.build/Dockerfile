FROM ubuntu:latest

RUN apt-get update \
 && apt-get install -y curl build-essential rsync openssh-client git wget \
 && apt-get clean

RUN VAGRANT_VERSION=$(wget -O- https://releases.hashicorp.com/vagrant/ | fgrep 'href="/vagrant' | head -1 | sed -r 's/.*([0-9].[0-9].[0-9]).*/\1/') \
 && curl -O https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.deb \
 && dpkg -i vagrant_${VAGRANT_VERSION}_x86_64.deb \
 && rm vagrant_${VAGRANT_VERSION}_x86_64.deb

RUN vagrant plugin install vagrant-aws \
 && vagrant plugin install vagrant-azure

WORKDIR /work

