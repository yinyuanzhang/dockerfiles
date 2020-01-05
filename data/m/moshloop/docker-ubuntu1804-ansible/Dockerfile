FROM ubuntu:18.04
LABEL maintainer="Moshe Immerman"
ENV container=docker
ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive
ARG ANSIBLE_VERSION=2.6.1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python-setuptools python-dev python-pip \
       software-properties-common \
       rsyslog systemd systemd-cron sudo \
       curl wget net-tools nano git \
       unzip zip tar gzip bzip2 \
       psmisc psutils bash lsof expect tree dos2unix xmlstarlet \
       ruby ruby-dev gcc genisoimage   \
       bats nmap openssl jq sshpass openssh-client libkrb5-3 libkrb5-dev \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean
RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf
COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

RUN mkdir -p /etc/ansible
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

RUN pip install --upgrade setuptools && pip install ansible==$ANSIBLE_VERSION ansible-dependencies

RUN wget -O inspec.deb  https://packages.chef.io/files/stable/inspec/2.2.20/ubuntu/18.04/inspec_2.2.20-1_amd64.deb && \
    dpkg -i inspec.deb && \
    rm inspec.deb

RUN wget -q -O /usr/bin/waiter https://github.com/moshloop/waiter/releases/download/1.1/waiter && \
    chmod +x /usr/bin/waiter

ADD entrypoint.sh /etc/entrypoint.sh

CMD /lib/systemd/systemd --system