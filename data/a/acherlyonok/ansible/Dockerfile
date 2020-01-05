FROM centos:centos7

USER root

ARG ANSIBLE_VERSION=2.6.19

RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y python-pip python-devel && \
    yum install -y gcc openssl-devel rsync make file autoconf automake libtool sshpass && \
    yum clean all

RUN pip install -U pip setuptools && \
    pip install requests termcolor jmespath jq

RUN mkdir -p /etc/ansible
RUN echo "[local]" >> /etc/ansible/hosts && \
    echo "localhost" >> /etc/ansible/hosts

RUN pip install awscli ansible==${ANSIBLE_VERSION} cryptography ansible-modules-hashivault docker-py boto boto3

# ADD ansible.cfg /etc/ansible/ansible.cfg

ENV PYTHONUNBUFFERED=1
ENV ANSIBLE_FORCE_COLOR=true
ENV ANSIBLE_GATHERING smart
ENV ANSIBLE_HOST_KEY_CHECKING false
ENV ANSIBLE_LOCAL_TEMP=/tmp
ENV ANSIBLE_RETRY_FILES_ENABLED false
ENV ANSIBLE_SSH_PIPELINING True
ENV ANSIBLE_STDOUT_CALLBACK yaml
ENV ANSIBLE_LOAD_CALLBACK_PLUGINS True
ENV ANSIBLE_ROLES_PATH=/ansible/roles

ENTRYPOINT ["/usr/bin/ansible-playbook"]
CMD ["--version"]