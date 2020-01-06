FROM openshift/jenkins-slave-base-centos7

# install "Inline with Upstream Stable" to get most current upstream stable release of Python 3
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm

# install Python 3.6 with pip
RUN yum install -y python36u python36u-pip
RUN pip3.6 install virtualenv
RUN pip3.6 install virtualenvwrapper
RUN yum -y install python36u-devel

# install wget and SQlite version 3.24
RUN yum install wget -y

RUN wget https://www.sqlite.org/2018/sqlite-autoconf-3240000.tar.gz
RUN tar xvfz sqlite-autoconf-3240000.tar.gz && cd sqlite-autoconf-3240000
RUN yum -y groupinstall "Development Tools" && \
    cd sqlite-autoconf-3240000 && ./configure && make

RUN rm -rf /usr/bin/sqlite3 && \
    mv /var/lib/origin/sqlite-autoconf-3240000/sqlite3 /usr/bin/

RUN /bin/cp -rf /var/lib/origin/sqlite-autoconf-3240000/.libs/ /usr/lib/ && \
     /bin/cp -rf /var/lib/origin/sqlite-autoconf-3240000/.libs/* /usr/lib64/


RUN python3.6 --version && sqlite3 --version

# change user to non-root OpenShift usage
RUN chown -R 1001:0 $HOME && \
    chmod -R g+rw $HOME
    
USER 1001
