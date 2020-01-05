FROM centos:7

RUN yum install -y epel-release \
    && yum update -y \
    && yum install -y lastpass-cli

ENTRYPOINT [ "/usr/bin/lpass" ]
