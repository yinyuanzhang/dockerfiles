FROM centos:7
MAINTAINER Juan Ramon Alfaro <jralfaro@oondeo.es>

RUN groupadd -g 1001 proxysql
RUN useradd -u 1001 -r -g 1001 -s /sbin/nologin \
		-c "Default Application User" proxysql

# check repository package signature in secure way
RUN export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \
	&& gpg --export --armor 430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A > ${GNUPGHOME}/RPM-GPG-KEY-Percona \
	&& rpmkeys --import ${GNUPGHOME}/RPM-GPG-KEY-Percona /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
	&& curl -L -o /tmp/percona-release.rpm https://repo.percona.com/centos/7/RPMS/noarch/percona-release-0.1-8.noarch.rpm \
	&& rpmkeys --checksig /tmp/percona-release.rpm \
	&& yum install -y /tmp/percona-release.rpm epel-release \
	&& rm -rf "$GNUPGHOME" /tmp/percona-release.rpm \
	&& rpm --import /etc/pki/rpm-gpg/PERCONA-PACKAGING-KEY \
	&& percona-release disable all \
&& percona-release enable ps-80 release && percona-release enable tools release

ENV PROXYSQL_VERSION="2.0.3-1.1.el7"  \
    PERCONA_VERSION="8.0.15-6.1.el7"

RUN yum install -y \
        percona-server-client-${PERCONA_VERSION} \
		proxysql2-${PROXYSQL_VERSION} \
		which \
		policycoreutils \
        pwgen wget jq \
	&& yum clean all \
    && rm -rf /var/cache/yum /var/lib/proxysql

ADD proxysql.cnf /etc/proxysql/proxysql.cnf
ADD proxysql-admin.cnf /etc/proxysql/
ADD proxysql-admin /usr/bin/proxysql-admin
RUN chmod +x /usr/bin/proxysql-admin

COPY proxysql-entry.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# COPY add_cluster_nodes.sh /usr/bin/add_cluster_nodes.sh
# RUN chmod a+x /usr/bin/add_cluster_nodes.sh

VOLUME /var/lib/proxysql

EXPOSE 3306 6032

CMD [""]
