FROM ubuntu:14.04

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0xcbcb082a1bb943db && \
echo "deb http://mariadb.mirror.iweb.com/repo/10.0/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/mariadb.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y curl git golang mariadb-server

# setup mariaDB
RUN  rm -rf /var/lib/apt/lists/* && \
sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
echo "mysqld_safe &" > /tmp/config && \
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config && \
bash /tmp/config && \
rm -f /tmp/config

# Set GOPATH/GOROOT environment variables
RUN mkdir -p /go
ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH

# Removed unnecessary packages
RUN apt-get autoremove -y

# Clear package repository cache
RUN apt-get clean all

EXPOSE 8080
EXPOSE 3306

RUN /usr/bin/mysqld_safe & \
    sleep 10s
