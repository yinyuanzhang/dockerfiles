FROM antik486/centos71
MAINTAINER Kerim Bekberov <bekberovkerim@gmail.com>

# Add nginx repositary to yum
ADD ./repo/nginx.repo /etc/yum.repos.d/

RUN yum -y update; yum clean all && \
    yum -y install nginx ; yum clean all && \
    rm -rf /var/tmp/*  && \
    echo "daemon off;" >> /etc/nginx/nginx.conf

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
WORKDIR /etc/nginx

EXPOSE 80

# Define default command.
CMD [ "/usr/sbin/nginx" ]
