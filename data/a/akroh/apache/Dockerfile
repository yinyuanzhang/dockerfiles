FROM akroh/centos:6

MAINTAINER Andrew Kroh (andy@crowbird.com)

RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm && \
    yum -y install puppet-3.7.4 git && \
    gem install librarian-puppet-simple --version 0.0.3

COPY Puppetfile /etc/puppet/
COPY site.pp /etc/puppet/manifests/
COPY www/* /var/www/html/

RUN cd /etc/puppet && \
    librarian-puppet install && \
    puppet apply /etc/puppet/manifests/site.pp && \
    service httpd stop && \
    yum clean all

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
