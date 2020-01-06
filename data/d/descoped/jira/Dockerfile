FROM descoped/atlassian-base
MAINTAINER Ove Ranheim <oranheim@gmail.com>

# Install Jira
ENV JIRA_VERSION 7.7.1

ENV JIRA_INST /opt/jira
ENV JIRA_HOME /var/atlassian-home

ENV UID jira
ENV GID atlassian

ADD configure.bash /configure
RUN chmod +x /configure

RUN curl -Lk http://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-$JIRA_VERSION.tar.gz -o /root/jira.tar.gz \
    && useradd -r --create-home --home-dir $JIRA_INST --groups $GID --shell /bin/bash $UID \
    && tar zxf /root/jira.tar.gz --strip=1 -C $JIRA_INST \
    && rm /root/jira.tar.gz \
    && echo "jira.home=$JIRA_HOME" > $JIRA_INST/atlassian-jira/WEB-INF/classes/jira-application.properties \
    && mv $JIRA_INST/conf/server.xml $JIRA_INST/conf/server-backup.xml

# Launching Jira
WORKDIR $JIRA_INST
VOLUME ["$JIRA_HOME"]

COPY entrypoint.bash /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 8080
CMD ["bin/start-jira.sh", "-fg"]
