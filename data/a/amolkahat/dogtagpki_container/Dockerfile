FROM fedora:latest

MAINTAINER Amol Kahat (akahat@redhat.com)
RUN dnf install -y rpm rpm-build gcc wget git libffi-devel redhat-rpm-config python3-yaml python3-devel\
    openssl-devel python3-lxml && dnf clean all
RUN ssh-keygen -f /root/.ssh/id_rsa -t rsa -N ''
RUN printf "Host *\n    StrictHostKeyChecking no" > /root/.ssh/config
RUN pip3 install linchpin lxml pyopenssl ansible==2.8.1 pytest-ansible==2.0.2 client pytest-ansible-playbook==0.4.1 pytest-logger pytest-autochecklog==0.2.0 configparser pytest-html

