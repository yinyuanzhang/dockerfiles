FROM centos:centos7

LABEL name="LIGO Koji RPM Test - Testing" \
      maintainer="Adam Mercer <adam.mercer@ligo.org>" \
      date="20190723" \
      support="Reference Platform"

# initialise metadata and update
RUN yum makecache && \
    yum -y update && \
    yum clean all

# add osg repository
RUN yum -y install https://repo.opensciencegrid.org/osg/3.4/osg-3.4-el7-release-latest.rpm

# add git-lfs repository
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | bash

# add lscsoft-backports repository
RUN echo "[lscsoft-backports]" > /etc/yum.repos.d/backports.repo && \
    echo "name = lscsoft-backports" >> /etc/yum.repos.d/backports.repo && \
    echo "baseurl = https://koji.ligo-la.caltech.edu/mash/lscsoft/7/\$basearch/backports/" >> /etc/yum.repos.d/backports.repo && \
    echo "enabled = 1" >> /etc/yum.repos.d/backports.repo && \
    echo "gpgcheck = 0" >> /etc/yum.repos.d/backports.repo

# add lscsoft-production repository
RUN echo "[lscsoft-production]" > /etc/yum.repos.d/production.repo && \
    echo "name = lscsoft-production" >> /etc/yum.repos.d/production.repo && \
    echo "baseurl = https://koji.ligo-la.caltech.edu/mash/lscsoft/7/\$basearch/production/" >> /etc/yum.repos.d/production.repo && \
    echo "enabled = 1" >> /etc/yum.repos.d/production.repo && \
    echo "gpgcheck = 0" >> /etc/yum.repos.d/production.repo

# add lscsoft-testing repository
RUN echo "[lscsoft-testing]" > /etc/yum.repos.d/testing.repo && \
    echo "name = lscsoft-testing" >> /etc/yum.repos.d/testing.repo && \
    echo "baseurl = https://koji.ligo-la.caltech.edu/mash/lscsoft/7/\$basearch/testing/" >> /etc/yum.repos.d/testing.repo && \
    echo "enabled = 1" >> /etc/yum.repos.d/testing.repo && \
    echo "gpgcheck = 0" >> /etc/yum.repos.d/testing.repo

# configure extra required repositories
RUN yum makecache && yum -y install \
      lscsoft-epel-config \
      lscsoft-grid-config \
      lscsoft-ius-config && \
    yum clean all

# install lscsoft-all and ldg-client
RUN yum makecache && \
    yum -y install lscsoft-all ldg-client && \
    yum clean all