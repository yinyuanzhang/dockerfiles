FROM ibandrea/jdk-oracle:8u121
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>

ENV CONFLUENCE_VERSION 6.0.6

ENV MYSQL_CONNECTOR_JAVA_VERSION 5.1.41

ENV CONFLUENCE_HOME     	/var/local/atlassian/confluence
ENV CONFLUENCE_INSTALL  	/usr/local/atlassian/confluence
ENV CONF_USER				confluence
ENV CONFLUENCE_INSTALLER	atlassian-confluence-$CONFLUENCE_VERSION.tar.gz

RUN deps=" \
	libtcnative-1 xmlstarlet \
	wget \
	" \
	set -x && \
    export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get upgrade -y $deps --no-install-recommends && \
	\
	useradd --create-home --shell /bin/bash $CONF_USER && \
	\
	cd /tmp && \
	wget --no-check-certificate http://www.atlassian.com/software/confluence/downloads/binary/$CONFLUENCE_INSTALLER && \
	mkdir -p $CONFLUENCE_INSTALL && \
	tar zxf $CONFLUENCE_INSTALLER --strip=1 -C $CONFLUENCE_INSTALL && \
	mkdir -p $CONFLUENCE_HOME && \
	echo -e "\nconfluence.home=$CONFLUENCE_HOME" >> "$CONFLUENCE_INSTALL/confluence/WEB-INF/classes/confluence-init.properties" && \
	sed -ri 's/CONF_USER.*/CONF_USER="$CONF_USER" ##/' $CONFLUENCE_INSTALL/bin/user.sh && \
	\
	wget --no-check-certificate http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION.tar.gz && \
	tar xzf mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION.tar.gz -C /tmp && \
	cp /tmp/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION-bin.jar $CONFLUENCE_INSTALL/confluence/WEB-INF/lib/ && \
	\
	chown -R $CONF_USER:$CONF_USER $CONFLUENCE_HOME && \
	chown -R $CONF_USER:$CONF_USER $CONFLUENCE_INSTALL && \
	\
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/var/local/atlassian/confluence"]

EXPOSE 8090

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/usr/local/atlassian/confluence/bin/start-confluence.sh", "-fg"]
