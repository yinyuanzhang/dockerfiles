FROM openjdk:8-jre-alpine

COPY target /target

ENV CONFIG_SERVER_PORT 7000

ENV CONFIG_DB_HOST mysql
ENV CONFIG_DB_PORT 3006
ENV CONFIG_DB_NAME 'config_api'
ENV CONFIG_DB_USER 'user'
ENV CONFIG_DB_PASS 'pass'

ENV CONFIG_HIBERNATE_DIALECT 'org.hibernate.dialect.MySQLDialect'
ENV CONFIG_JPA_DB 'mysql'
ENV CONFIG_JPA_SHOW_SQL 'false'

EXPOSE ${CONFIG_SERVER_PORT}

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/target/ari-config-api-0.1-SNAPSHOT.jar"]