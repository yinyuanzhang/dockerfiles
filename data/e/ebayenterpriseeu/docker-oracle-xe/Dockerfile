FROM esepublic/baseimage

MAINTAINER Sergey Kolodyazhnyy <skolodyazhny@ebay.com>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1 net-tools bc && \
    apt-get --purge autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

ADD oracle /oracle

RUN ln -s /usr/bin/awk /bin/awk && \
    mkdir /var/lock/subsys && \
    mv /oracle/chkconfig /sbin/chkconfig && \
    chmod 755 /sbin/chkconfig

RUN cat /oracle/oracle-xe_11.2.0-1.0_amd64.deba* > /oracle/oracle-xe_11.2.0-1.0_amd64.deb

RUN dpkg --install /oracle/oracle-xe_11.2.0-1.0_amd64.deb

RUN cp /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora.tmpl && \
    mv /oracle/init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \
    mv /oracle/initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \
    printf 8080\\n1521\\noracle\\noracle\\ny\\n | /etc/init.d/oracle-xe configure

ENV ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe \
    ORACLE_SID=XE

EXPOSE 1521
EXPOSE 8080

CMD /oracle/startup.sh && /sbin/my_init
