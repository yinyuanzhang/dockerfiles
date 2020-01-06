FROM        centos:latest


RUN         yum install -y etcd

VOLUME      /data
EXPOSE      2379 2380 4001 7001


ENV         ADVERTISE_URL   advertise_url
ENV         PEER_URL        peer_url
ENV         NAME            name
ENV         CLUSTER         initial_cluster
ENV         CLUSTER_TK      cluster_token


LABEL maintainer="Matt Kimberley <matthew.kimberley@fasthosts.com>" \
    version="1"

CMD         /bin/rm -rf /var/lib/etcd2
CMD         /usr/bin/etcd       -data-dir=/data \
                                -name ${NAME} \
                                -advertise-client-urls http://${ADVERTISE_URL}:2379 \ 
                                -listen-client-urls http://0.0.0.0:2379 \
                                -initial-advertise-peer-urls http://${ADVERTISE_URL}:2380 \
                                -listen-peer-urls http://0.0.0.0:2380 \
                                -initial-cluster-token ${CLUSTER_TK} \
                                -initial-cluster ${CLUSTER}\
                                -initial-cluster-state new \
