FROM centos
LABEL maintainer lincolnb@uchicago.edu


RUN yum update -y

RUN yum install epel-release -y

#RUN yum install facter -y
RUN yum install http://mirror.grid.uchicago.edu/pub/puppet5/7/x86_64/puppet-agent-5.5.10-1.el7.x86_64.rpm -y

RUN yum install nmap-ncat -y

COPY minimon /usr/local/bin/minimon

CMD ["/usr/local/bin/minimon"]
