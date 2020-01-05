FROM amazonlinux:1
MAINTAINER Caleb Collins <ccollins@imm.com>

RUN yum -y update && yum -y install \
        postfix \
        httpd24 \
        mysql56 \
        php71 \
        php71-gd \
        php71-intl \
        php71-json \
        php71-mbstring \
        php71-mcrypt \
        php71-mysqlnd \
        php71-pdo \
        php71-pecl-imagick \
        php71-xml

RUN groupadd -g 1000 ec2-user && \
      adduser -g ec2-user -u 1000 -s /bin/bash ec2-user && \
      sed -ri -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
        -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
        /etc/httpd/conf/httpd.conf

COPY scripts /scripts
RUN chmod -R 755 /scripts

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
