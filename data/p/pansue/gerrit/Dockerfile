FROM centos:7.6.1810
MAINTAINER TCL COMMUNICATION SCM

# Add Gerrit packages repository
RUN rpm -i https://gerritforge.com/gerritforge-repo-1-2.noarch.rpm


# Install OS pre-prequisites, OpenJDK and Gerrit in two subsequent transactions
# (pre-trans Gerrit script needs to have access to the Java command)

RUN yum -y install initscripts  java-1.8.0-openjdk

#Install gerrit
RUN yum -y install gerrit-2.15.7-1

#Download the mysql-connector
RUN curl -o /var/gerrit/lib/mysql-connector-java-5.1.43.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.43/mysql-connector-java-5.1.43.jar

ADD entrypoint.sh /

RUN   /entrypoint.sh init &&\
    rm -f /var/gerrit/etc/{ssh,secure}* && rm -Rf /var/gerrit/{static,index,logs,data,index,cache,git,db,tmp}/* && chown -R gerrit:gerrit /var/gerrit && \
    yum -y clean all

RUN usermod -u 500 gerrit &&  groupmod -g 500 gerrit

USER gerrit

#ENV CANONICAL_WEB_URL=

# Allow incoming traffic
EXPOSE 29418 8080

VOLUME ["/var/gerrit/git", "/var/gerrit/index", "/var/gerrit/cache", "/var/gerrit/db", "/var/gerrit/etc"]

ENTRYPOINT ["/entrypoint.sh"]

