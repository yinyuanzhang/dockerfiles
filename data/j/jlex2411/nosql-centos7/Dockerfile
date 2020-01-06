FROM centos:7
LABEL Maintainer "nguyentruonghuy93@gmail.com"

EXPOSE 1337-1338 27017 6379 3000-3010
WORKDIR /root
RUN yum -y install git \
    nano \
    dos2unix \
    unzip \
    net-tools \
    libpng-devel \
    epel-release
RUN touch /etc/yum.repos.d/mongodb-org-3.6.repo \
    && printf '[mongodb-org-3.6]\nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.6/x86_64/\ngpgcheck=1\nenabled=1\ngpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc' > /etc/yum.repos.d/mongodb-org-3.6.repo \
    && curl -sL https://rpm.nodesource.com/setup_10.x | bash - \
    && yum -y install mongodb-org \
      nodejs \
      redis \
      supervisor \
    && sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf \
    && sed -i 's/bind 127.0.0.1/bind 0.0.0.0/g' /etc/redis.conf \
    && sed -i 's/protected-mode yes/protected-mode no/g' /etc/redis.conf \ 
    && mkdir -p /var/www/projects 
RUN npm install -g pm2
COPY config/supervisord.conf /etc/supervisord.conf
WORKDIR /var/www/projects     
CMD ["/usr/bin/supervisord"]
