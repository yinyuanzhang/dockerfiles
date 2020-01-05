FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD admin123
ENV MYSQL_DATABASE curso

ADD datos/cargaDatos.sql /docker-entrypoint-initdb.d/cargaDatos.sql