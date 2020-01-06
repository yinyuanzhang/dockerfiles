FROM centos:centos6.7

ENV JAVA_VERSION 1.7.0
RUN yum -y update && \
    yum -y install java-${JAVA_VERSION}-openjdk wget zip && \
    yum install -y --enablerepo=centosplus libselinux-devel httpd epel-release && \
    yum -y install ipython python-psutil python-pycurl && \
    yum clean all

# Add install utility for AEM
ADD aemInstaller.py /aem/aemInstaller.py
