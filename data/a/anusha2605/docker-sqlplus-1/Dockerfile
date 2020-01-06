FROM sflyr/ubuntu
MAINTAINER sflyr

RUN apt-get -y update
RUN apt-get -y install libaio1 unzip rlwrap
ADD basic-10.2.0.5.0-linux-x64.zip /
ADD sqlplus-10.2.0.5.0-linux-x64.zip /
ADD sdk-10.2.0.5.0-linux-x64.zip /
ADD jdbc-10.2.0.5.0-linux-x64.zip /
RUN unzip basic-10.2.0.5.0-linux-x64.zip
RUN unzip sqlplus-10.2.0.5.0-linux-x64.zip
RUN unzip sdk-10.2.0.5.0-linux-x64.zip
RUN unzip jdbc-10.2.0.5.0-linux-x64.zip

ENV LD_LIBRARY_PATH /instantclient_10_2

# CMD /instantclient_11_2/sqlplus <user>/<password>@//xxx.yyy.eu-west-1.rds.amazonaws.com:1521/ORCL
CMD sleep 1; rlwrap /instantclient_10_2/sqlplus $URL
