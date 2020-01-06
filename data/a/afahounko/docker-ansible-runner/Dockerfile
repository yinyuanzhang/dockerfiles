FROM fedora:latest

MAINTAINER Afahounko Danny <danny@afahounko.com>

RUN dnf update -y && \
    dnf -y install python python-netaddr python2-pip  openssl-devel openssl  jq && \
    dnf clean all

RUN pip install --upgrade pip && \
    pip install Jinja2 requests && \
    pip install ansible

RUN mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

# default command: display Ansible version
CMD [ "ansible", "--version" ]
