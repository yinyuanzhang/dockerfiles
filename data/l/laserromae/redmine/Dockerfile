FROM centos:latest

RUN yum -y clean all && yum -y install ImageMagick ImageMagick-devel apr-devel apr-util-devel autoconf automake bison bzip2 curl curl-devel gcc gcc-c++ git httpd-devel ipa-pgothic-fonts libcurl-devel libffi-devel libtool libyaml-devel make openssl-devel patch postgresql-devel readline readline-devel sendmail sqlite-devel subversion sudo which zlib zlib-devel

RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby

COPY src/install.sh /
RUN chmod 755 /install.sh && /install.sh

COPY conf/database.yml /var/www/redmine/config/
COPY conf/configuration.yml /var/www/redmine/config/
COPY conf/passenger.conf /etc/httpd/conf.d/
COPY src/entrypoint.sh /

#RUN cd /var/www/redmine; bundle install --without development test postgresql sqlite mysql; bundle exec rake generate_secret_token

EXPOSE 9000

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

