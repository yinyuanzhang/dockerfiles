FROM centos:7

RUN yum makecache fast \
  && yum -y install java-1.8.0-openjdk unzip \
  && yum clean all

VOLUME /app

WORKDIR /app

CMD ["/bin/bash"]
