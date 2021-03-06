# OOI UI
# <https://github.com/asascience-open/ooi-ui>
# Author: RPS ASA
# Usage: <https://github.com/asascience-open/ooi-ui/wiki/Automated-Deployment-(Docker)>

FROM centos:centos6
MAINTAINER The CentOS Project <cloud-ops@centos.org>

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install git; yum clean all
RUN yum -y install sudo; yum clean all
RUN yum -y install which; yum clean all
RUN yum -y install tar; yum clean all
RUN yum -y update gmp; yum clean all
RUN yum -y install wget; yum clean all
RUN yum -y install gcc; yum clean all

RUN yum -y install openssl-devel; yum clean all
RUN yum -y install libxml2-devel; yum clean all
RUN yum -y install libxslt-devel; yum clean all
RUN yum -y install libcurl-devel; yum clean all
RUN yum -y install sqlite-devel; yum clean all
RUN yum -y install readline-devel; yum clean all
RUN yum -y install db4-devel; yum clean all
RUN yum -y install db4-devel-static; yum clean all

RUN yum -y install ctags-etags; yum clean all
RUN yum -y install tmux; yum clean all
RUN yum -y install java-1.7.0-openjdk-devel; yum clean all
RUN yum -y groupinstall 'Development Tools'; yum clean all

# HDF5 Installation
WORKDIR /tmp
RUN wget http://www.hdfgroup.org/ftp/HDF5/current/bin/RPMS/hdf5-1.8.14-1.with.szip.encoder.el6.x86_64.rpm
RUN yum -y install hdf5-1.8.14-1.with.szip.encoder.el6.x86_64.rpm; yum clean all
RUN rm -rf hdf5-1.8.14-1.with.szip.encoder.el6.x86_64.rpm

# NetCDF4 Installation
WORKDIR /tmp
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.3.2.tar.gz
RUN tar -zxvf netcdf-4.3.2.tar.gz -C /usr/local/src/
RUN rm -rf netcdf-4.3.2.tar.gz
WORKDIR /usr/local/src/netcdf-4.3.2
RUN ./configure --prefix=/usr/local --enable-netcdf-4 --enable-dap --enable-shared && /usr/bin/make && /usr/bin/make install

# Python Installation
WORKDIR /tmp
RUN wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tgz && tar -xzvf Python-2.7.6.tgz -C /usr/local/src/
RUN rm -rf Python-2.7.6.tgz
WORKDIR /usr/local/src/Python-2.7.6
RUN ./configure --prefix=/usr/local && /usr/bin/make && /usr/bin/make altinstall
RUN ln -s /usr/local/bin/python2.7 /usr/local/bin/python27

# Virutal Environment Installation
WORKDIR /root
RUN wget https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh
RUN chmod +x virtualenv-burrito.sh
RUN ./virtualenv-burrito.sh
WORKDIR /root
RUN chmod +x /root/.venvburrito/startup.sh
RUN source /root/.venvburrito/startup.sh && mkvirtualenv --no-site-packages --python=/usr/local/bin/python27 ooiui
RUN rm -rf virtualenv-burrito.sh

# OOI UI Installation
RUN git clone https://github.com/asascience-open/ooi-ui.git /root/ooi-ui
WORKDIR /root/ooi-ui
ENV WORKON_HOME /root/.virtualenvs
RUN /bin/bash -c "source /root/.venvburrito/startup.sh \
    && workon ooiui \
    && pip install -r requirements.txt"

# Install Node.js
WORKDIR /tmp
RUN wget http://nodejs.org/dist/v0.10.35/node-v0.10.35-linux-x64.tar.gz
WORKDIR /usr/local
RUN tar --strip-components 1 -xzf /tmp/node-v0.10.35-linux-x64.tar.gz
RUN rm -rf /tmp/node-v0.10.35-linux-x64.tar.gz
WORKDIR /root/ooi-ui
RUN npm install -g grunt-cli
RUN npm install -g bower
RUN npm install

RUN bower install -s --allow-root
RUN grunt

ADD start_ooi-ui.sh /root/ooi-ui/start_ooi-ui.sh
RUN chmod +x /root/ooi-ui/start_ooi-ui.sh

EXPOSE 5000

CMD [ "/bin/bash", "-c", "/root/ooi-ui/start_ooi-ui.sh" ]

