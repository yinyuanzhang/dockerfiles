FROM centos:latest
MAINTAINER Arie Bregman, abregman@redhat.com, bregman.arie@gmail.com

# Without reinstalling python-setuptools, the installation of ksgen simply hangs forever. 

RUN \
  rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm && \
  yum install -y python-pip python-devel openssh-server git gcc && \
  mkdir -p /var/run/sshd && \
  /usr/bin/pip install -U ansible==1.9.2 && \
  yum remove -y python-setuptools && \
  yum install -y python-setuptools && \
  /usr/bin/git clone https://github.com/redhat-openstack/khaleesi.git && \
  /usr/bin/cp /khaleesi/ansible.cfg.example /khaleesi/ansible.cfg && \
  cd /khaleesi/tools/ksgen && \
  /usr/bin/python setup.py develop

# create host keys
RUN ssh-keygen -b 1024 -t rsa -f /etc/ssh/ssh_host_key
RUN ssh-keygen -b 1024 -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -b 1024 -t dsa -f /etc/ssh/ssh_host_dsa_key

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
