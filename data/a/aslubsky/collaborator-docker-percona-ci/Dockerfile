
FROM percona:5.7

ENV MYSQL_ROOT_PASSWORD=tests
ENV MYSQL_DATABASE=elearn_et_tests
ENV MYSQL_USER=tests
ENV MYSQL_PASSWORD=tests

RUN printf '[mysqld]\nskip-host-cache\nskip-name-resolve\nsql_mode='"'"''"'"'\n' > /etc/my.cnf.d/docker.cnf
