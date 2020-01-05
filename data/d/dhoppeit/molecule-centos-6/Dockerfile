FROM centos:6

LABEL maintainer="Dennis Hoppe"

ENV container docker

RUN yum upgrade -y \
    && yum -y install initscripts iproute nc \
    && yum clean all

VOLUME [ "/sys/fs/cgroup" ]

CMD ["/sbin/init"]
