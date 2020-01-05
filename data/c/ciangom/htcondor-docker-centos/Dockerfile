# Dockerizing HTCondor nodes

FROM       centos:centos7
MAINTAINER Manuel Ciangottini <manuel.ciangottini@gmail.com>
ENV        TINI_VERSION v0.9.0
EXPOSE  5000
EXPOSE  22

#--- Environment variables
ENV USER="amsuser"
ENV USER_HOME="/home/amsuser"

#RUN curl -sS http://get.onedata.org/oneclient.sh | bash

#--- Patch yum for docker
RUN yum install -y yum-plugin-ovl

#--- Install rpms
RUN yum-config-manager --enable onedata; \
yum install -y epel-release; \
yum update -y; yum clean all; \
yum -y install initscripts; \
yum -y install freetype fuse sudo glibc-devel glibc-headers; \
yum -y install man nano emacs openssh-server openssl098e libXext libXpm curl wget vim; \
yum -y install git gsl-devel freetype-devel libSM libX11-devel libXext-devel make gcc-c++; \
yum -y install gcc binutils libXpm-devel libXft-devel boost-devel; \
yum -y install ncurses ncurses-devel; \
yum clean all; \
yum install -y cvs openssh-clients;

RUN yum -y install systemd; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f /lib/systemd/system/local-fs.tar get.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*; \
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ “/sys/fs/cgroup” ]

WORKDIR /root

# Setting up a user
RUN adduser $USER -d $USER_HOME && echo "$USER:user" | chpasswd && \
    echo "$USER ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USER && \
    chmod 0440 /etc/sudoers.d/$USER
RUN chown -R $USER $USER_HOME

COPY dot-bashrc $USER_HOME/.bashrc
RUN chown $USER $USER_HOME/.bashrc; \
mkdir $USER_HOME/.ssh; \
chown $USER:$USER $USER_HOME/.ssh

# CONDOR
ADD     https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin/tini

WORKDIR /etc/yum.repos.d
RUN	wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-rhel7.repo; \
wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo; \
wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor; \
rpm --import RPM-GPG-KEY-HTCondor; \
yum-config-manager --enable onedata; \
yum install -y condor-all ; \
yum install -y python-pip && pip install supervisor supervisor-stdout && \
        # HEALTHCHECKS
        mkdir -p /opt/health/master/ /opt/health/executor/ /opt/health/submitter/ && \
        pip install Flask

RUN     pip install --upgrade pip && \
#        pip uninstall -y distribute && \
        pip install --upgrade setuptools

RUN curl -sS http://get.onedata.org/oneclient.sh | bash

USER    root
WORKDIR /root
RUN     chmod u+x /sbin/tini

COPY 	supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY    condor_config /etc/condor/condor_config
COPY    master_healthcheck.py /opt/health/master/healthcheck.py
COPY    executor_healthcheck.py /opt/health/executor/healthcheck.py
COPY    submitter_healthcheck.py /opt/health/submitter/healthcheck.py
COPY 	sshd_config /etc/ssh/sshd_config
COPY    run.sh /usr/local/sbin/run.sh

RUN     mkdir -p /mnt/onedata; \
mkdir -p /var/log/dodas

RUN     ln -s /usr/lib64/condor /usr/lib/condor; \
ln -s /usr/libexec/condor /usr/lib/condor/libexec

ENTRYPOINT ["/sbin/tini", "--", "/usr/local/sbin/run.sh"]
