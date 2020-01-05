FROM ubuntu:14.04

# Install Percona Server, client, toolkit and xtrabackup.
RUN \
  apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A && \
  echo "deb http://repo.percona.com/apt `lsb_release -cs` main" > /etc/apt/sources.list.d/percona.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y percona-server-server-5.6 percona-server-client-5.6 percona-toolkit percona-xtrabackup

# Empty mysql data dir, so that the init script can start from a clean slate
RUN rm -rf /var/lib/mysql/*

# Define mountable directories.
VOLUME ["/etc/mysql", "/var/lib/mysql"]

# Add a mysql config. 
ADD mysql/my.cnf /etc/mysql/my.cnf

# Add scripts
ADD scripts/* /usr/local/bin/

# Define default command.
CMD ["start_mysqld.sh"]

# Expose ports.
EXPOSE 3306
