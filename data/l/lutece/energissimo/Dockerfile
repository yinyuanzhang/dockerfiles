FROM lutece/builder as builder

# define the fully qualified artifact of the site
ARG site=site-energissimo-1.0.0-SNAPSHOT

# build and install the plugin
WORKDIR /plugin
ADD energissimo-plugin/pom.xml /plugin/pom.xml
ADD energissimo-plugin/src /plugin/src
ADD energissimo-plugin/webapp /plugin/webapp
RUN mvn install


# build the site and assemble the webapp
WORKDIR /app
ADD energissimo-site/pom.xml /app/pom.xml
ADD energissimo-site/src /app/src
ADD energissimo-site/webapp /app/webapp
RUN mvn lutece:site-assembly

# change default user
RUN  sed -i 's/root/admin/' /app/target/${site}/WEB-INF/conf/db.properties


# run the database initialization script
WORKDIR /app/target/${site}/WEB-INF/sql
RUN  /etc/init.d/mysql start && \
    sleep 5s && \
    mysql -uroot -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'motdepasse'; GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';FLUSH PRIVILEGES;CREATE DATABASE lutece" && \
    sleep 5s && \
    ant && sleep 5s && \
    /etc/init.d/mysql stop 

RUN mv /app/target/${site}/ /var/lib/tomcat8/webapps/energissimo


COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]
