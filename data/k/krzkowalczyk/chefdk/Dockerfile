FROM ubuntu:18.04
MAINTAINER Krzysztof Kowalczyk
LABEL chefdk="3.8.14"
LABEL vagrant="2.2.5"

ARG CHANNEL=stable
ARG CHEF_VERSION=3.8.14
ARG VAGRANT_VERSION=2.2.5
ENV DEBIAN_FRONTEND=noninteractive \
    PATH=/opt/chefdk/bin:/opt/chefdk/embedded/bin:/root/.chefdk/gem/ruby/2.6.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Run the entire container with the default locale to be en_US.UTF-8
RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

RUN apt-get update && \
    apt-get install -y git graphviz rsync ssh vim-tiny wget jq && \
    ln -s /usr/bin/vi /usr/bin/vim && \
    wget --content-disposition "http://packages.chef.io/files/${CHANNEL}/chefdk/${CHEF_VERSION}/ubuntu/18.04/chefdk_${CHEF_VERSION}-1_amd64.deb" -O /tmp/chefdk.deb && \
    dpkg -i /tmp/chefdk.deb && \
    wget --content-disposition "https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.deb" -O /tmp/vagrant.deb && \
    dpkg -i /tmp/vagrant.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*log /var/log/apt/* /var/lib/dpkg/*-old /var/cache/debconf/*-old

CMD ["/bin/bash"]
