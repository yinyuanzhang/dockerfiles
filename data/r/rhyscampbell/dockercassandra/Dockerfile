FROM centos:8
LABEL maintainer="github.com/rhysmeister"
RUN yum update -y

COPY resources/cassandra.repo /etc/yum.repos.d/
RUN yum clean all
RUN yum install initscripts -y && yum install cassandra -y

# Fixes su - cannot open session issue
RUN sed -i '/^session.*include.*system-auth$/s/^/#/g' /etc/pam.d/su
RUN cat /etc/pam.d/su

RUN sed -i -r -e 's@^rpc_address.*$@rpc_address: 0\.0\.0\.0@' /etc/cassandra/conf/cassandra.yaml
RUN sed -i -r -e 's@^# broadcast_rpc_address.*$@broadcast_rpc_address: 127\.0\.0\.1@' /etc/cassandra/conf/cassandra.yaml
RUN sed -i -r -e 's@^authenticator.*$@authenticator: PasswordAuthenticator@' /etc/cassandra/conf/cassandra.yaml
RUN sed -i -r -e 's@^authorizer.*$@authorizer: CassandraAuthorizer@' /etc/cassandra/conf/cassandra.yaml

EXPOSE 9042/tcp
EXPOSE 9160/tcp
EXPOSE 7199/tcp

# Don't use su in the CMD but rather USER dockerfile intruction
USER cassandra
CMD ["cassandra", "-f"]
