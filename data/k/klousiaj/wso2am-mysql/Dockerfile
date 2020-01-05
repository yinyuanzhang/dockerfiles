FROM mysql:latest
MAINTAINER J.P. Klousia

ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE WSO2AM_STATS_DB
ENV MYSQL_USER wso2am
ENV MYSQL_PASSWORD wso2am

# disable some problem sql-mode values that were added with 5.7
COPY assets/etc/mysql/conf.d/my.cnf /etc/mysql/conf.d/my.cnf
# create the API Manager Stats DB automatically.
COPY assets/dbscripts/mysql.sql /docker-entrypoint-initdb.d/mysql.sql