FROM centos

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm  \
    && yum update -y \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip \
    && ln -s /usr/bin/python3.6 /usr/bin/python3 \
    && ln -s /usr/bin/pip3.6 /usr/bin/pip3 \
    && pip3 install --upgrade pip \
    && pip3 install mock pytest tox wheel \
    && rm -rfv /var/cache/yum \
    && rm -rfv ~/.cache/pip
