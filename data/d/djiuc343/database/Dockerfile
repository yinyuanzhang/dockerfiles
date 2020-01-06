FROM mysql:5

ENV MYSQL_ROOT_PASSWORD 123
ENV MYSQL_DATABASE      mikeDemo
ENV MYSQL_USER          rest_service
ENV MYSQL_PASSWORD      123

ADD seedData.sql /docker-entrypoint-initdb.d
