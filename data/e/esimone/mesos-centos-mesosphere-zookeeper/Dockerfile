FROM esimone/mesos-centos-mesosphere

RUN yum install -y mesosphere-zookeeper \
 && yum --enablerepo=* clean all \
 && rm -rf /var/cache/yum

ENV ZOOCFGDIR=/etc/zookeeper/conf \
    ZOODATADIR=/var/lib/zookeeper \
    ZOOMYID=/var/lib/zookeeper/myid

WORKDIR /opt/mesosphere/zookeeper

EXPOSE 2181 2888 3888

VOLUME $ZOODATADIR

ENTRYPOINT [ "/opt/mesosphere/zookeeper/bin/zkServer.sh", "start-foreground" ]

