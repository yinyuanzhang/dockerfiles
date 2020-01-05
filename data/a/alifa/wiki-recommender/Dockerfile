FROM centos:centos6

MAINTAINER ali.fathieh@gmail.com

# Enable EPEL for Node.js
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# Install Node...
RUN yum install -y npm

# Copy app to /src
COPY . /src

# Install app and dependencies into /src
RUN cd /src; npm install
# RUN npm install

EXPOSE 9005

# CMD cd /src && node ./app.js
CMD cd /src && npm start