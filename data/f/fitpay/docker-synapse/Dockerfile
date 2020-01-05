FROM centos:7

MAINTAINER Scott Stevelinck <scott@fit-pay.com>

RUN yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel
RUN yum install -y libyaml-devel libffi-devel openssl-devel make
RUN yum install -y bzip2 autoconf automake libtool bison iconv-devel sqlite-devel
RUN yum install -y which haproxy
RUN yum clean all

RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -
RUN curl -L get.rvm.io | bash -s stable
RUN /usr/local/rvm/bin/rvm reload && /usr/local/rvm/bin/rvm install 2.2.4

RUN mkdir -p /synapse
RUN /usr/local/rvm/bin/rvm all do gem install synapse -v 0.15.1 --no-document

ADD haproxy.sh /haproxy.sh
RUN chmod 755 /haproxy.sh

ENV RUBY_VERSION 2.2.4
ADD /synapse.conf.json /synapse-default.conf.json
ADD run.sh /run.sh
RUN chmod 755 /run.sh

ENTRYPOINT ["/run.sh"]
CMD ["run"]
