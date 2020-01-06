FROM mysql
WORKDIR /db
COPY . /db
COPY ./DatabaseInitialization /docker-entrypoint-initdb.d/
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE library
EXPOSE 3306
CMD ["mysqld"]
