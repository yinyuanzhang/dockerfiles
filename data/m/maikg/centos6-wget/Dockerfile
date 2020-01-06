FROM centos:6
RUN yum -y install wget

RUN wget -O /tmp/epel-repo.rpm https://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum -y localinstall /tmp/epel-repo.rpm

RUN rm -f /tmp/epel-repo.rpm
