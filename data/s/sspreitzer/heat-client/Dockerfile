FROM centos:7

RUN yum install -y centos-release-openstack-mitaka && \
    yum install -y python-heatclient python-swiftclient && \
    yum clean all

CMD "heat"
