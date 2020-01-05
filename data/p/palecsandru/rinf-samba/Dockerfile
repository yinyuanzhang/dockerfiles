FROM centos:centos7.4.1708

###############################################################################
# System dependencies
###############################################################################
RUN yum --enablerepo=extras install epel-release -y
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update -y && yum install -y \
    vim \
    net-tools
RUN mkdir -p /dataroot
RUN chmod 777 /dataroot
COPY fix-permissions.sh ./
VOLUME ["/dataroot"]

###############################################################################
# Samba
###############################################################################
RUN yum install -y \
        samba \
        samba-client \
        samba-common
COPY ./samba.sh /usr/bin/samba.sh
COPY ./smb.conf /etc/samba/
RUN chmod 777 /usr/bin/samba.sh
EXPOSE 139 445

################################################################################
## Start script
################################################################################
COPY start.sh /
RUN chmod 777 /start.sh

###############################################################################
# Make sure that everything is written to disk
###############################################################################
RUN sync

###############################################################################
# Start container services
###############################################################################
ENTRYPOINT /start.sh & /bin/bash
