FROM atlassian/confluence-server
ADD https://cdn.mysql.com//Downloads/Connector-J/mysql-connector-java-5.1.47.tar.gz /tmp/mysql-connector-java-5.1.47.tar.gz

RUN cd /tmp && tar -xzf mysql-connector-java-5.1.47.tar.gz 
RUN cd /tmp/mysql-connector-java-5.1.47 && mv /tmp/mysql-connector-java-5.1.47/mysql-connector-java-5.1.47.jar /opt/atlassian/confluence/confluence/WEB-INF/lib
RUN rm -rf /tmp/mysql-connector-java-5.1.47*