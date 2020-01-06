FROM centos:centos7

RUN yum -y update && \
    yum -y install \
        lsof \
        epel-release \
        git \
        python-simplejson \
        openssh-server \
        openssh-clients \
        koji; yum clean all

RUN /usr/bin/ssh-keygen -A
ENV USER_CONFIG_DIR /opt/koji-clients/users/kojiadmin

EXPOSE 22 
ADD bin/ /usr/local/bin/

ENV COMMON_CONFIG /config
RUN chmod +x /usr/local/bin/*
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN mkdir /var/run/sshd
RUN echo 'root:mypassword' | chpasswd

ENTRYPOINT /usr/local/bin/entrypoint.sh
