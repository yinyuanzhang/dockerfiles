FROM centos:7

RUN yum makecache && yum install -y \
    sshpass openssh-clients \
    && yum clean all

CMD ["/bin/bash"]
