FROM mysql:5.6.46

ENV MYSQL_ALLOW_EMPTY_PASSWORD=true \
    MYSQL_DATABASE=circle_test \
    MYSQL_HOST=127.0.0.1 \
    MYSQL_ROOT_HOST=% \
    MYSQL_USER=root

RUN echo '\n\
[mysqld]\n\
collation-server = utf8_unicode_ci\n\
init-connect="SET NAMES utf8"\n\
character-set-server = utf8\n\
innodb_flush_log_at_trx_commit=2\n\
sync_binlog=0\n\
innodb_use_native_aio=0\n\
datadir = /dev/shm/mysql\n\
performance_schema = ON\n\
log_output = TABLE\n\
log_queries_not_using_indexes = ON\n\
slow_query_log = ON\n\
general_log = ON\n\
' >> /etc/mysql/my.cnf

COPY ./sys_1.5.1_56_inline.sql /docker-entrypoint-initdb.d/sys_1.5.1_56_inline.sql
