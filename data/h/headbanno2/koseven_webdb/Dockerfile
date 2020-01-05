FROM mysql/mysql-server:5.6

RUN echo 'max_heap_table_size=68M' | awk \
    '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' \
    /etc/my.cnf > /tmp/my.cnf \
    && mv /tmp/my.cnf /etc/my.cnf

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
