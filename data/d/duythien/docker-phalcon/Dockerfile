FROM ubuntu
MAINTAINER "Thien Tran" <fcduythien@gmail.com>
ENV container docker

RUN apt-get update && apt-get install -yqq \
    git \
    libxml2-dev \
    python \
    build-essential \
    make \
    gcc \
    python-dev \
    locales \
    python-pip
#

ENV DEBIAN_FRONTEND noninteractive
ENV  MYSQL_PASSWORD root

#Adding shell scripts
ADD scripts/mysql.sh /tmp/mysql.sh
ADD scripts/nginx.sh /tmp/nginx.sh
ADD scripts/php.sh /tmp/php.sh
ADD scripts/phalcon.sh /tmp/phalcon.sh
ADD run.sh /tmp/run.sh

RUN chmod 755 /tmp/*.sh

#Install Nginx
RUN ./tmp/nginx.sh

#install php-fpm
RUN ./tmp/php.sh


#install mysql
#RUN ./tmp/mysql.sh

#install phalcon
#RUN ./tmp/phalcon.sh

##Setup ssh


#RUN apt-get install -yqq openssh-server
#RUN mkdir -p /var/run/sshd
#RUN chmod 0755 /var/run/sshd

# Create and configure vagrant user
#RUN useradd --create-home -s /bin/bash vagrant
#WORKDIR /home/vagrant

# Configure SSH access
#RUN mkdir -p /home/vagrant/.ssh
#RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys

#RUN chown -R vagrant: /home/vagrant/.ssh
#RUN echo -n 'vagrant:vagrant' | chpasswd

# Enable passwordless sudo for the "vagrant" user
#RUN echo 'vagrant ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vagrant
#CMD /usr/sbin/sshd -D -o UseDNS=no -o UsePAM=no

EXPOSE 80

# Copy site into place.
COPY www /usr/share/nginx/html/www
ADD templates/nginx/default.conf /etc/nginx/sites-enabled/default

CMD ["nginx", "-g", "daemon off;"]
CMD ["sh", "/tmp/run.sh"]

#CMD ["php5-fpm" ,"-D"]
#ENTRYPOINT /usr/sbin/php5-fpm -D
#CMD ["/bin/bash", "/tmp/run.sh"]