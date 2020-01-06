# Pull base image
FROM centos:7

# Locale
RUN sed -i -e "s/LANG=\"en_US.UTF-8\"/LANG=\"ja_JP.UTF-8\"/g" /etc/locale.conf

# Timezone
RUN cp -p /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# System update
RUN yum -y update

# Install Tools
RUN yum install -y \
        git \
        less \
        vim \
        curl \
        net-tools

# Install mysql
RUN rpm -Uvh https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm && \
    yum install -y --enablerepo=mysql57-community \
        mysql-community-server

# Cache cleaning
RUN yum clean all

# User
RUN groupmod --gid 1000 mysql && usermod mysql --uid 1000 --gid 1000

# Httpd setting(mod_php)
COPY ./conf/my.cnf /etc/my.cnf
RUN chmod 644 /etc/my.cnf
WORKDIR /var/lib/mysql

VOLUME ["/var/log/"]

# Listen port
EXPOSE 3306

# Startup
ENTRYPOINT ["/usr/sbin/mysqld"]
