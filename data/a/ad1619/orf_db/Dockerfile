FROM mysql:8.0

ENV  MYSQL_DATABASE orf
ENV  MYSQL_ROOT_PASSWORD password


COPY dump.sql /docker-entrypoint-initdb.d/dump.sql

CMD ["mysqld", "--default-authentication-plugin=mysql_native_password"]



