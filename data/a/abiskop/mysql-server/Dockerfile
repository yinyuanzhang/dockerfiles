FROM mirkokiefer/ubuntu-base

RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe > /etc/apt/sources.list
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >> /etc/apt/sources.list
RUN apt-get update

# taken from https://github.com/kstaken/dockerfile-examples/blob/master/mysql-server/mysql-setup.sh
# Keep upstart from complaining
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -f -s /bin/true /sbin/initctl

RUN apt-get install -y mysql-server

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init", "mysqld"]
