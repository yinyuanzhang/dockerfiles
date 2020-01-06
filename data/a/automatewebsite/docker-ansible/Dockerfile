FROM ubuntu:16.04

LABEL MAINTAINER=<hello@automate.website>

ARG ANSIBLE_VERSION=2.5
ARG DEBIAN_FRONTEND=noninteractive

ENV ANSIBLE_CONFIG=/ansible/ansible.cfg

RUN echo "deb http://ppa.launchpad.net/ansible/ansible-$ANSIBLE_VERSION/ubuntu xenial main" | tee /etc/apt/sources.list.d/ansible.list \
    && echo "deb-src http://ppa.launchpad.net/ansible/ansible-$ANSIBLE_VERSION/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/ansible.list \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7BB9C367 \
    && apt-get update \
    && apt-get install -y ansible

RUN apt-get install -y \
      nano \
      dnsutils \
      traceroute \
      curl

RUN rm -rf /var/lib/apt/lists/*

CMD [ "ansible-playbook", "--version" ]