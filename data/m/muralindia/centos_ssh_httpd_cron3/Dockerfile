FROM centos:centos7
MAINTAINER MD
ENV container docker
RUN yum -y update; yum clean all
RUN yum -y install openssh-server initscripts httpd links openssh-clients systemd python-setuptools cronie
RUN easy_install supervisor
RUN sshd-keygen
COPY hello-cron /etc/cron.d/hello-cron
RUN echo 'root:passw0rd' | chpasswd
Expose 80 22
COPY supervisord.conf /etc/supervisor/supervisord.conf
CMD ["/usr/bin/supervisord"]


