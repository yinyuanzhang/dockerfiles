FROM dock0/service
MAINTAINER Jon Chen <bsd@voltaire.sh>

ENV ETCD_DATA_DIR "/srv/etcd/"

VOLUME ["/srv/etcd"]

ADD https://dl.bintray.com/jchen/docku/latest/etcd /usr/sbin/etcd

ADD run /service/etcd/run
