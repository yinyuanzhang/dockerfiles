FROM centos:7

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="ansible-ci" \
      org.label-schema.description="Image centos 7 with ansible for CI test" \
      org.label-schema.url="http://andradaprieto.es" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/jandradap/ansible-ci" \
      org.label-schema.vendor="Jorge Andrada Prieto" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0" \
      maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \
      org.label-schema.docker.cmd="docker run -it -v /sys/fs/cgroup:/sys/fs/cgroup:ro jorgeandrada/ansible-ci:centos7systemd bash"

RUN yum install -y epel-release \
  && yum makecache fast \
  && yum install -y \
    libselinux-python \
    util-linux \
    selinux-policy \
    firewalld \
    jq \
    git \
    python2-pip \
    ca-certificates \
    sshpass \
    openssl \
    sudo \
  && pip install --upgrade \
    setuptools \
    pip \
    ansible \
    jmespath \
    jsonpath \
    jinja2 \
    PyYAML \
    paramiko \
    cryptography \
  && yum clean all \
  && mkdir /etc/ansible

COPY ansible.cfg /etc/ansible/

ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
