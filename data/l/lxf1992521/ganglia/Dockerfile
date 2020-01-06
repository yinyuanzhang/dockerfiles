FROM centos:7
RUN yum install -y epel-release && yum install -y ganglia-gmond && yum remove -y epel-release && yum clean all
COPY startup.sh /
ENTRYPOINT [ "bash", "/startup.sh" ]
