FROM mysql:5.5

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y aptitude apt-utils

RUN mv /etc/mysql/my.cnf /etc/mysql/my.cnf.bak; \
  DEBIAN_FRONTEND=noninteractive aptitude install -y git make gcc g++ libmysqlclient-dev; \
  mv /etc/mysql/my.cnf.bak /etc/mysql/my.cnf

RUN mkdir -p /var/tmp/beanstalkd_udf /var/tmp/beanstalk-client
RUN git clone https://github.com/deepfryed/beanstalk-client.git /var/tmp/beanstalk-client
RUN (cd /var/tmp/beanstalk-client && make install)
RUN git clone https://github.com/scr34m/beanstalkd_udf.git /var/tmp/beanstalkd_udf
RUN ln -s /usr/include/mysql /usr/local/include/mysql
RUN mkdir -p /opt/local/lib/mysql5/mysql
RUN ln -s /usr/local/mysql/lib/plugin /opt/local/lib/mysql5/mysql/plugin
RUN (cd /var/tmp/beanstalkd_udf && make && make install)

RUN apt-get remove --purge -y git make gcc g++ aptitude && apt-get autoclean && apt-get clean

COPY ./initdb/functions.sql /docker-entrypoint-initdb.d/
