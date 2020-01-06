FROM sdal/c7
MAINTAINER "Aaron D. Schroeder" <aschroed@vt.edu>

LABEL name="CentOS Base Image" \
    vendor="CentOS" \
    license="GPLv2" \
    build-date="20170301"

ENV container docker

# Update System Image
RUN \
  yum update -y && \
  yum upgrade -y

RUN  yum install -y epel-release; yum clean all

RUN \
  yum install -y initscripts && \
  yum install -y openssh openssh-server openssh-clients openssl-libs && \
  yum install -y sssd && \
  yum install -y emacs nano htop && \
  yum install -y authconfig; yum clean all

# Fix locale
RUN yum reinstall glibc-common -q -y && \
    yum reinstall -y glibc; yum clean all
RUN localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# SSH & LDAP
RUN systemctl enable sshd
COPY sssd.conf /etc/sssd
COPY journal.conf /etc/systemd/system/sssd.service.d
COPY rm_nologin.sh /etc/profile.d
COPY userFolders.sh /usr/bin
COPY custom.target /etc/systemd/system
RUN chmod +x /usr/bin/userFolders.sh
RUN mkdir -p /etc/systemd/system/custom.target.wants
COPY userFolders.service /etc/systemd/system/custom.target.wants
#RUN systemctl isolate custom.target
RUN ln -sf /etc/systemd/system/custom.target /etc/systemd/system/default.target

COPY groups /
RUN cat /groups >> /etc/group

# set proper perms
RUN chmod 600 /etc/sssd/sssd.conf
# nasty hack #1
RUN mkdir -p /etc/openldap/cacerts
# configure the rest of auth mechanisms, including the download of our CA cert
RUN authconfig --nostart --enablesssd --enablesssdauth --enablelocauthorize --update --ldaploadcacert=http://cert.vbi.vt.edu/vbi-cacert.pem
# nasty hack #2, not sure why manual authconfig doesn't create it
RUN ln -sf /etc/openldap/cacerts/authconfig_downloaded.pem /etc/openldap/cacerts/ef25a808.0
# finally, update and restart. we also enable creation of home dirs for new users
RUN authconfig --enablemkhomedir --update
RUN systemctl enable sssd

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/lib/systemd/systemd"]
