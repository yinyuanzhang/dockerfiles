FROM centos:centos7

MAINTAINER "myasuda" <myasuda@uchida.co.jp>

RUN yum install -y epel-release.noarch

# install packages
RUN yum update -y
RUN yum install -y openssh-server supervisor rpm-build redhat-rpm-config make wget

# user settings
RUN echo "root:root" | chpasswd
RUN useradd jenkins -m -d /build
RUN echo "jenkins:jenkins" | chpasswd

RUN mkdir -p /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd

RUN mkdir -p /var/run/supervisord
COPY supervisord.conf /etc/supervisord.conf

RUN mkdir -p /build/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN echo '%_topdir %(echo $HOME)/rpmbuild' > /build/.rpmmacros
RUN chown -R jenkins:jenkins /build

# install oracle jdk 1.8.0
ENV JDK_VERSION 8u91
ENV JDK_BUILD_NO b14
ENV JDK_PRM jdk-${JDK_VERSION}-linux-x64.rpm
RUN wget -q \
         --no-check-certificate \
         --no-cookies \
         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
         http://download.oracle.com/otn-pub/java/jdk/${JDK_VERSION}-${JDK_BUILD_NO}/${JDK_PRM} && \
    rpm -ihv ${JDK_PRM} && \
    rm -f ${JDK_PRM}

# install git subversion
RUN yum -y install git subversion

EXPOSE 22

CMD ["/usr/bin/supervisord"]

