FROM		hauptmedia/hadoop-base

ENV     	HDFS_DATANODE_ROOT_DIR=/var/hdfs/datanode

ADD		conf/core-site.xml	${HADOOP_INSTALL_DIR}/etc/hadoop/core-site.xml
ADD		conf/hdfs-site.xml	${HADOOP_INSTALL_DIR}/etc/hadoop/hdfs-site.xml

ADD		docker-entrypoint.sh /usr/local/sbin/docker-entrypoint.sh

VOLUME		["${HDFS_DATENODE_ROOT_DIR}"]


# TCP	50010	dfs.datanode.address		port for data transfer
# TCP	50020	dfs.datanode.ipc.address	ipc server
# TCP	50075	dfs.datanode.http.address	http server
# TCP	50475	dfs.datanode.https.address	https server

EXPOSE 50010 50020 50075 50475

ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]

CMD ["bin/hdfs", "datanode"]

