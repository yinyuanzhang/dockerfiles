FROM lutece/builder as builder

# define the fully qualified artifact of the site
ARG site=site-suggest-demo-1.0.0-SNAPSHOT

# (mvn local proxy...)
# ADD settings.xml /root/.m2/

# build the site and assemble the webapp
WORKDIR /app
ADD pom.xml /app/pom.xml
ADD dump.sql /app/dump.sql
# ADD webapp /app/webapp
RUN mvn lutece:site-assembly

# change default user
RUN  sed -i 's/root/admin/' /app/target/${site}/WEB-INF/conf/db.properties

RUN mv /app/target/${site}/ /var/lib/tomcat8/webapps/suggest

# run the database initialization script
RUN  /etc/init.d/mysql start && \
    sleep 5s && \
    mysql -uroot -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'motdepasse'; GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';CREATE DATABASE lutece" && \
    sleep 5s && \
    mysql -uroot -pmotdepasse lutece < dump.sql && \
    sleep 5s && \
    /etc/init.d/mysql stop 

COPY entrypoint.sh /entrypoint.sh

ENV LUTECE_DB_NAME=lutece
ENV LUTECE_DB_USER=admin
ENV LUTECE_DB_PWD=motdepasse


ENTRYPOINT ["sh", "/entrypoint.sh"]




