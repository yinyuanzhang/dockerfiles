FROM centos

RUN yum update -y && \
        yum install -y open-vm-tools && \
  yum clean all

CMD ["/usr/bin/vmtoolsd"]
