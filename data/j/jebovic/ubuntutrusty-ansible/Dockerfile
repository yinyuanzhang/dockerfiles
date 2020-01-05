FROM ubuntu:14.04

MAINTAINER Jérémy Baumgarth

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python-software-properties \
       software-properties-common \
       rsyslog sudo \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Upgrade python version to 2.7.10
RUN apt-add-repository -y ppa:fkrull/deadsnakes-python2.7 \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       python2.7 \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Install Ansible.
RUN apt-add-repository -y ppa:ansible/ansible \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       ansible \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Install Ansible inventory file
RUN mkdir -p /etc/ansible \
    && echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

COPY initctl_custom .
RUN chmod +x initctl_custom && rm -fr /sbin/initctl && ln -s /initctl_custom /sbin/initctl

CMD /bin/sh
