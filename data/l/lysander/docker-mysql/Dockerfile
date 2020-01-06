FROM phusion/baseimage
MAINTAINER Lysander Vogelzang <lysander@nuclyus.nl>

# Install MariaDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0xcbcb082a1bb943db && \
  echo "deb http://mariadb.mirror.iweb.com/repo/10.0/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/mariadb.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server && \
  rm -rf /var/lib/apt/lists/*

# Remove the default data dir for mysql,
#	make sure the UID of user mysql matches that of the user myql on the host system (5003 in our case)
#	and set file permission

RUN \
  rm -rf /var/lib/mysql/* && \
  usermod -u 5003 mysql && \ 
  chown mysql:mysql /var/run/mysqld/ && \
  chmod ug+rw /var/run/mysqld/ && \
  mkdir /data/ && \
  chown mysql:mysql /data/ && \ 
  chmod ug+rw /data/

# ADD our manual configuration
ADD my.cnf /etc/mysql/my.cnf

# And make it only readably for user mysql, but not world-writeable (than mysql will refuse to use the config)
RUN \
  chown mysql:mysql /etc/mysql/my.cnf && \ 
  chmod 730 /etc/mysql/my.cnf
  
# Define mountable directories.
VOLUME ["/data"]

# Expose ports.
EXPOSE 3306

# Execute mysql as user mysql
USER mysql

# Make sure docker subs have access
GRANT SELECT  ON *.* TO user@'172.17.%' IDENTIFIED BY '95k(77z{G2S*R7J';

# Define default command.
CMD ["/usr/bin/mysqld_safe"]

# NOTE! This container removes the default data for database, as it's meant to be used
#	by an already initialized data directory. Therefore, to initialize with a new database,
#	run this docker with the mysql_install_db script like:
#	
#	docker run -v PATH:/data lysander/docker-mysql mysql_install_db --user=mysql --datadir=/data
#	
#