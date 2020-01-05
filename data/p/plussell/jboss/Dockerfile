# This image is extended from https://github.com/jboss-dockerfiles/wildfly
# extending instructions are there
FROM jboss/wildfly

# environment variables
ENV JDBC_MD5 bc23a03d813af3f7ac44b8e7a5cb0d54
ENV JDBC_VER 5.1.42

# add database conndection
COPY files /opt/jboss/files
RUN cd $HOME && \
    curl -O -L https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-$JDBC_VER.tar.gz && \
    md5sum mysql-connector-java-$JDBC_VER.tar.gz | grep $JDBC_MD5 && \
    tar -xzf mysql-connector-java-$JDBC_VER.tar.gz && \
    mkdir -p $JBOSS_HOME/modules/system/layers/base/com/mysql/main && \
    ln -s $HOME/mysql-connector-java-$JDBC_VER/mysql-connector-java-5.1.42-bin.jar $JBOSS_HOME/modules/system/layers/base/com/mysql/main/mysql-connector-java.jar && \
    cp $HOME/files/module.xml $JBOSS_HOME/modules/system/layers/base/com/mysql/main/ && \
    sed -i -e '/<datasources>/ r $HOME/files/datasource.xml' $JBOSS_HOME/standalone/configuration/standalone.xml && \
    sed -i -e '/<drivers>/ r $HOME/files/driver.xml' $JBOSS_HOME/standalone/configuration/standalone.xml

# Cleanup
USER root
RUN rm -rf /opt/jboss/files
USER jboss

EXPOSE 8080 9990

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
