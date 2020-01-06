FROM centos:8
MAINTAINER dongyupu@foxmail.com

# Configuration variables.
USER root
ENV RUN_USER root
ENV RUN_GROUP root
ENV JIRA_HOME     /var/atlassian/jira
ENV JIRA_INSTALL  /opt/atlassian/jira
ENV JIRA_VERSION  8.5.0

EXPOSE 8080
WORKDIR $JIRA_HOME
#install Opnejdk-1.8.0 and jira-software 8.5.1
RUN set -x \
    && yum -y update \
    && yum -y groupinstall Fonts \
    && yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel \
    && echo -e "export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el7_7.x86_64" ~/.bash_profile \
    && echo -e "export PATH=$PATH:$JAVA_HOME/bin" ~/.bash_profile \
    && echo -e "export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar" ~/.bash_profile \
    && source ~/.bash_profile \
    && mkdir -p "${JIRA_INSTALL}/conf/Catalina" \
    && curl -Ls "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-core-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner \
    && chown -R $RUN_USER:$RUN_GROUP $JIRA_INSTALL \
    && yum clean all

#enterypoint
CMD ["/opt/atlassian/jira/bin/start-jira.sh", "-fg"]
