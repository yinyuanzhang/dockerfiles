FROM mysql:5.7
MAINTAINER leon_xi@163.com

#设置免密登录
ENV MYSQL_ROOT_PASSWORD 1234

#将所需文件放到容器中
COPY setup.sh /docker-entrypoint-initdb.d/setup.sh
COPY init_database_duan.sql /mysql/init_database_duan.sql
COPY init_database_duan_privileges.sql /mysql/init_database_duan_privileges.sql

RUN chmod +x /docker-entrypoint-initdb.d/setup.sh
