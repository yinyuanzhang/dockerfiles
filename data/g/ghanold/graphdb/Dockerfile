# orientdb
#
# VERSION: see `TAG`
# Using centos (yum)
FROM centos:centos7
MAINTAINER Gregg Hanold "ghanold79@gmail.com"

#Create oseraf system user
RUN mkdir i -p /opt/oseraf && \
groupadd -r oseraf -g 498 && \
useradd -u 498 -r -g oseraf -d /opt/oseraf -s /sbin/nologin -c "Docker image user" oseraf && \
chown -R oseraf:oseraf /opt/oseraf

USER root
RUN yum -y update; yum clean all

# install system deps
RUN yum -y install wget
RUN yum -y install tar
RUN yum -y install install java-1.7.0-openjdk-devel
RUN yum -y install git
RUN yum -y install ant

# install orientdb
USER oseraf
ENV ROOT /opt/oseraf
ENV ORIENT_URL https://github.com/orientechnologies/orientdb.git

RUN cd ${ROOT} \
	&& git clone ${ORIENT_URL} \
	&& cd orientdb \
	&& ant clean install \
	&& cd ..
ENV ORIENT_VERSION orientdb-community-2.0
RUN mv ${ROOT}/orientdb ${ROOT}/${ORIENT_VERSION}
USER root
RUN ln -s ${ROOT}/releases/${ORIENT_VERSION} ${ROOT}/orientdb \
        && ln -s ${ROOT}/orientdb/bin/* /usr/local/bin/ \
	&& mkdir /usr/local/log
USER oseraf
RUN cd ${ROOT}/orientdb \
	&& rm -rf config \
	&& rm -rf databases

# cleanup
USER root
RUN yum clean all \
	&& rm -rf /opt/oseraf/linux /var/lib/apt/lists/* /tmp/* /var/tmp/*

# configure system
EXPOSE 2424
EXPOSE 2480
# start orientdb
USER oseraf
CMD ["/usr/local/bin/server.sh"]
#

