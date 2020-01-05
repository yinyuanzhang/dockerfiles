FROM ubuntu:bionic
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg
ARG ANSIBLE_VERSION=2.6.1
ARG SYSTOOLS_VERSION=3.0
ENV DEBIAN_FRONTEND=noninteractive
ADD ansible.cfg /etc/ansible/ansible.cfg
RUN apt-get update && \
    apt-get install -y python-setuptools python-pip python-dev build-essential jq libkrb5-dev krb5-user wget curl openssh-client sshpass genisoimage bats git inetutils-ping dnsutils sudo nano && \
    pip install \
    ansible==$ANSIBLE_VERSION ansible-run ansible-dependencies && \
    wget -O systools.deb https://github.com/moshloop/systools/releases/download/$SYSTOOLS_VERSION/systools_${SYSTOOLS_VERSION}_amd64.deb && dpkg -i systools.deb && \
    install_bin https://master.dockerproject.org/linux/x86_64/docker \
                https://github.com/moshloop/waiter/releases/download/1.1/waiter

ENTRYPOINT ["/usr/local/bin/ansible-playbook"]