FROM mysql:latest

ARG sakila_file
ARG db_name
ENV MYSQL_DATABASE ${db_name}
COPY ${sakila_file} /docker-entrypoint-initdb.d/
