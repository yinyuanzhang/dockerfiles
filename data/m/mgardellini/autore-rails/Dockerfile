FROM centos:centos6
MAINTAINER Mariano Gardellini <mariano.gardellini@gmail.com>

ENV RUBYVER 2.1.3

RUN yum groupinstall -y 'development tools'
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y curl-devel nano sqlite-devel libyaml-devel vim htop readline-devel zlib-devel libffi-devel openssl-devel
RUN yum install -y git
RUN yum install -y wget unzip tar
RUN yum install -y postgresql-libs postgresql-devel

RUN cd /opt && git clone https://github.com/sstephenson/rbenv.git && git clone https://github.com/sstephenson/ruby-build.git /opt/rbenv/plugins/ruby-build

COPY nginx /etc/init.d/nginx
RUN chmod 700 /etc/init.d/nginx
COPY nginx.conf /opt/nginx/conf/nginx.conf

COPY ruby-setup.sh /tmp/ruby-setup.sh
RUN /tmp/ruby-setup.sh ${RUBYVER}

RUN mkdir /root/.ssh
COPY id_rsa.pub /root/.ssh/id_rsa.pub
COPY id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa.pub
RUN chmod 600 /root/.ssh/id_rsa
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN export PATH="/opt/rbenv/bin:$PATH"
RUN export RBENV_ROOT=/opt/rbenv
RUN eval "$(rbenv init -)"

ADD ./run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

EXPOSE 3456

ENTRYPOINT ["/usr/local/bin/run"]
