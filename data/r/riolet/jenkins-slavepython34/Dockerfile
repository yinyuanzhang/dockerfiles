FROM openshift/jenkins-slave-base-centos7

MAINTAINER Rohana Rezel <rohana.rezel@riolet.com>

RUN yum install -y epel-release
RUN yum install -y python34
RUN yum install -y python34-pip
RUN pip3 install virtualenv
RUN pip3 install setuptools
RUN chown -R 1001:0 $HOME && \
    chmod -R g+rw $HOME
USER 1001

