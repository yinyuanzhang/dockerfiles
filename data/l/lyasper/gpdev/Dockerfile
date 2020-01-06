FROM lyasper/sshd:latest

RUN yum -y update
RUN yum -y groupinstall "Development Tools"
RUN yum -y install readline-devel zlib-devel \
           curl-devel apr-devel libevent-devel \
           libxml2-devel bzip2-devel python-devel \
           openssl-devel cmake which
RUN yum install -y iproute net-tools epel-release
RUN yum install -y python-pip python-psutil
RUN pip install --no-cache-dir lockfile paramiko setuptools
RUN yum install -y ruby-devel gcc make rpm-build rubygems
RUN yum clean all
RUN gem install --no-ri --no-rdoc fpm
CMD  ["/usr/sbin/sshd", "-D"]

