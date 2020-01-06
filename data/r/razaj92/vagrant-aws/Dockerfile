FROM ubuntu:xenial

RUN \
apt-get update && \
apt-get install -y curl python-dev python-pip libyaml-dev kmod ssh && \
curl -O https://releases.hashicorp.com/vagrant/2.0.0/vagrant_2.0.0_x86_64.deb && \
dpkg -i vagrant_2.0.0_x86_64.deb && \
pip install awscli && \
vagrant plugin install vagrant-aws && \
vagrant box add dummy https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box

ENTRYPOINT [""]
