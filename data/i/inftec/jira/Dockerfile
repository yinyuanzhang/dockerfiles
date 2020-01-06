# This builds a JIRA Docker container

FROM inftec/ubuntu-java:8u171
MAINTAINER Fabian Gut <fabian.gut@inftec.ch>, InfTec GmbH
MAINTAINER Martin Meyer <martin.meyer@inftec.ch>, InfTec GmbH

# Install Curl
RUN apt-get --allow-releaseinfo-change update && \
    apt-get install -y \
        curl sudo && \
    apt-get autoclean

# Download MYSQL Driver
ENV MYSQL_DRIVER_VERSION 5.1.46
RUN curl -Lks http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz -o /root/mysql-connector.tar.gz
        
# Install JIRA
ENV JIRA_VERSION 8.3.0
RUN curl -Lks https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${JIRA_VERSION}.tar.gz -o /root/jira.tar.gz
RUN mkdir /opt/jira && tar xzf /root/jira.tar.gz --strip=1 -C /opt/jira && rm /root/jira.tar.gz

# Install MYSQL Driver
RUN tar xzf /root/mysql-connector.tar.gz --strip=1 --wildcards '*/mysql-connector-java*.jar' && \
    mv mysql-connector-java*.jar /opt/jira/lib && \
    rm /root/mysql-connector.tar.gz

# Copy assets
COPY assets/config/ /opt/jira-setup/config/
COPY assets/setup/ /opt/jira-setup/setup/
COPY assets/jira.init /opt/jira-setup/jira.init
RUN cp /opt/jira/conf/server.xml /opt/jira-setup/config/server.xml
RUN chmod 755 /opt/jira-setup/jira.init

VOLUME /opt/jira-home
EXPOSE 8080
ENTRYPOINT ["/opt/jira-setup/jira.init"]
CMD ["jira:start"]


