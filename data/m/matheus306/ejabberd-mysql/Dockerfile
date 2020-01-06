FROM mysql:5.6

ENV MYSQL_USER ejabberd
ENV MYSQL_PASSWORD 123123
ENV MYSQL_ROOT_PASSWORD 123123

COPY mysql.sql /docker-entrypoint-initdb.d/
COPY aec_2.sql /docker-entrypoint-initdb.d/