FROM kakinari/centos-ja:latest
ENV container docker
RUN rpm -ivh http://dev.mysql.com/get/var/tmp/mysql80-community-release-el7-2.noarch.rpm;\
yum-config-manager --disable mysql80-community;\
yum-config-manager --enable mysql57-community;\
yum -y install openssh-clients  openssl mysql-community-client nmap-ncat;\
yum upgrade -y;\
yum clean all; \
rm -rf /var/cache/yum/*;
VOLUME /sys/fs/cgroup
CMD /usr/sbin/init
WORKDIR /root
