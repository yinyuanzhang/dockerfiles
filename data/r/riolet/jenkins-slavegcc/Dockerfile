FROM openshift/jenkins-slave-base-centos7

MAINTAINER Rohana Rezel <rohana.rezel@riolet.com>

RUN yum groupinstall -y 'Development Tools'
RUN yum install -y wget
RUN wget http://ftp.gnu.org/gnu/bison/bison-3.0.4.tar.xz
RUN tar xvf bison-3.0.4.tar.xz && cd  bison-3.0.4 && ./configure && make && make install
RUN yum install -y flex-devel
RUN yum install -y valgrind
RUN chown -R 1001:0 $HOME && \
    chmod -R g+rw $HOME

USER 1001
