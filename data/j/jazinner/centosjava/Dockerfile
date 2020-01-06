FROM centos
MAINTAINER Jason Shepherd <jshepher@redhat.com>
RUN curl http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo > /etc/yum.repos.d/epal-apache-maven.repo
RUN yum install --assumeyes centos-release-SCL && ( \
     echo "update"; \
     echo "install java-1.7.0-openjdk"; \
     echo "install java-1.7.0-openjdk-devel"; \
     echo "install apache-maven"; \
     echo "install git"; \
     echo "install unzip"; \
     echo "run" ) | yum shell --assumeyes && yum clean all --assumeyes
ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk.x86_64
ENTRYPOINT ["/bin/bash"]
