FROM ceph/daemon:latest-mimic

RUN rpm -ivh http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-2.el7.noarch.rpm && \
    yum install --assumeyes zabbix-sender && yum clean all --assumeyes && rm -rf /var/cache/yum
