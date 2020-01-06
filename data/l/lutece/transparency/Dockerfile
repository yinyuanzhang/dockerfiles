FROM lutece/builder as builder

# define the fully qualified artifact of the site
ARG site=site-transparency-1.0.0-SNAPSHOT

# get http proxy from build command
ARG http_proxy
ENV http_proxy=${http_proxy}
ARG https_proxy
ENV https_proxy=${https_proxy}



# build the site and assemble the webapp
WORKDIR /app
ADD pom.xml /app/pom.xml
ADD src /app/src
ADD webapp /app/webapp
RUN mvn lutece:site-assembly

# change default user
RUN  sed -i 's/root/admin/' /app/target/${site}/WEB-INF/conf/db.properties

# run the database initialization script
WORKDIR /app/target/${site}/WEB-INF/sql
RUN  /etc/init.d/mysql start && \
    sleep 5s && \
    mysql -uroot -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'motdepasse'; GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';FLUSH PRIVILEGES;CREATE DATABASE lutece" && \
    sleep 5s && \
    mysql -uadmin -pmotdepasse lutece < /app/src/sql/dump.sql && \
    sleep 5s && \
    /etc/init.d/mysql stop 

RUN mv /app/target/${site}/ /var/lib/tomcat8/webapps/transparency


COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]
