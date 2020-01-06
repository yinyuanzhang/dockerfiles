FROM centos:7
MAINTAINER kawabatas

ENV DG_VERSION 9_9_13
ENV DG_FILE linux2.6-dg${DG_VERSION}.tar.gz
ENV DG_DIR dg${DG_VERSION}
ENV DG_URL http://delegate.hpcc.jp/anonftp/DeleGate/bin/linux/latest/${DG_FILE}
ENV DG_HOME /home/delegate

WORKDIR $DG_HOME

RUN set -xe \
    && yum update -y \
    && yum install -y wget \
    && wget ${DG_URL} -O ${DG_FILE} \
    && tar xzf ${DG_FILE} \
    && ln -s ${DG_HOME}/${DG_DIR}/DGROOT/bin/${DG_DIR} /bin/delegated \
    && rm -rf /var/cache/yum/* \
    && yum clean all

COPY delegated.conf ${DG_HOME}/${DG_DIR}/DGROOT/bin/

ENTRYPOINT ["/bin/delegated"]
