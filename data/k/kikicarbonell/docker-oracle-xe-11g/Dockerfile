FROM ubuntu:14.04

MAINTAINER Maksym Bilenko <sath891@gmail.com>

# get rid of the message: "debconf: unable to initialize frontend: Dialog"
ENV DEBIAN_FRONTEND noninteractive

ADD chkconfig /sbin/chkconfig
ADD oracle-install.sh /oracle-install.sh
ADD init.ora /
ADD initXETemp.ora /

# Prepare to install Oracle
RUN apt-get update && apt-get install -y -q libaio1 net-tools bc curl rlwrap openssh-server && \
apt-get clean && \
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* && \
ln -s /usr/bin/awk /bin/awk && \
mkdir /var/lock/subsys && \
chmod 755 /sbin/chkconfig && \
/oracle-install.sh && \
mkdir /var/run/sshd && \
echo 'root:admin' | chpasswd && \
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
echo "export VISIBLE=now" >> /etc/profile

# see issue #1
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe
ENV PATH $ORACLE_HOME/bin:$PATH
ENV ORACLE_SID=XE

EXPOSE 1521
EXPOSE 8080
EXPOSE 22
VOLUME ["/u01/app/oracle"]

ENV processes 500
ENV sessions 555
ENV transactions 610

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD [""]
