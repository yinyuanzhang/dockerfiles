FROM jboss/wildfly:8.1.0.Final

USER root

RUN yum install -y epel-release && \
    yum install -y xmlstarlet && \
    yum clean all

USER jboss
