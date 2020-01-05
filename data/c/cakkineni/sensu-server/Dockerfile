FROM centos:7

ADD sensu_repo.repo /etc/yum.repos.d/sensu_repo.repo
RUN yum update -y && yum install -y sensu rubygems python

WORKDIR /tmp
ADD run.sh /tmp/run.sh
RUN chmod +x /tmp/run.sh
CMD ./run.sh

EXPOSE 4567 5671