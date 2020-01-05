FROM ibandrea/jdk-oracle:8u121
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>

ENV JIRA_VERSION 7.3.2

ENV MYSQL_CONNECTOR_JAVA_VERSION 5.1.41

ENV JIRA_HOME     	/var/local/atlassian/jira
ENV JIRA_INSTALL  	/usr/local/atlassian/jira
ENV JIRA_USER	  	jira
ENV JIRA_INSTALLER	atlassian-jira-software-$JIRA_VERSION.tar.gz

RUN deps=" \
	libtcnative-1 xmlstarlet \
	wget \
	" \
	set -x && \
    export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get upgrade -y $deps --no-install-recommends && \
	\
	useradd --create-home --shell /bin/bash $JIRA_USER && \
	\
	cd /tmp && \
	wget --no-check-certificate http://www.atlassian.com/software/jira/downloads/binary/$JIRA_INSTALLER && \
	mkdir -p $JIRA_INSTALL && \
	tar zxf $JIRA_INSTALLER --strip=1 -C $JIRA_INSTALL && \
	mkdir -p $JIRA_HOME && \
	echo -e "\njira.home=$JIRA_HOME" >> "$JIRA_INSTALL/atlassian-jira/WEB-INF/classes/jira-application.properties" && \
	sed -ri 's/JIRA_USER.*/JIRA_USER="$JIRA_USER" ##/' $JIRA_INSTALL/bin/user.sh && \
	\
	wget --no-check-certificate http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION.tar.gz && \
	tar xzf mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION.tar.gz -C /tmp && \
	cp /tmp/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION-bin.jar $JIRA_INSTALL/lib/ && \
	\
	chown -R $JIRA_USER:$JIRA_USER $JIRA_HOME && \
	chown -R $JIRA_USER:$JIRA_USER $JIRA_INSTALL && \
	\
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/var/local/atlassian/jira"]

EXPOSE 8080

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/usr/local/atlassian/jira/bin/start-jira.sh", "-fg"]

