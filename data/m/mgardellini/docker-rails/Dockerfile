FROM centos:centos6
MAINTAINER Mariano Gardellini <mariano.gardellini@gmail.com>

RUN useradd developer

RUN yum groupinstall -y 'development tools'
RUN yum install -y mysql-devel wget tar

RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm 
RUN yum install -y libyaml-devel libffi-devel readline-devel

USER developer 

# install RVM and ruby
ENV RVM_DIR /home/developer/.rvm
ENV PATH $PATH:$RVM_DIR/scripts/rvm
ENV PATH $PATH:$HOME/.rvm/bin
RUN /bin/sh -l -c "echo 'source ~/.profile' >> /home/developer/.bash_profile"
RUN /bin/sh -l -c "curl -L get.rvm.io | bash -s stable"
RUN /bin/sh -l -c "rvm requirements"
RUN /bin/sh -l -c "rvm install 2.1.1 -C --with-iconv-dir=$RVM_DIR,--without-readline"

USER root

RUN yum install -y rubygems

ADD ./run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

EXPOSE 3000

COPY ./simple-api /simple-api
RUN chmod -R 777 /simple-api

USER developer

ENTRYPOINT ["/usr/local/bin/run"]
