FROM centos:latest

COPY entrypoint.sh /entrypoint.sh

RUN yum -y install hdparm epel-release \
  && yum -y install fpaste \
  && chown 0:0 /entrypoint.sh \
  && chmod 770 /entrypoint.sh

ENTRYPOINT /entrypoint.sh
