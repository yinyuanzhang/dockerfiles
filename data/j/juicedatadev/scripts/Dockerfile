FROM centos:6

RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6 && \
  yum update -y && \
  yum install -y centos-release-scl && \
  rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo && \
  curl -L -o /tmp/bats.tar.gz https://github.com/sstephenson/bats/archive/master.tar.gz && \
  tar xvf /tmp/bats.tar.gz -C /tmp/ && \
  /tmp/bats-master/install.sh /usr && \
  rm -rf /tmp/bats-master bats.tar.gz && \
  yum install -y busybox util-linux python27-python rh-python35-python rh-python36-python && \
  yum clean all -y && \
  rm -rf /var/cache/*
