FROM centos:7

#RUN yum update --disableplugin=fastestmirror

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install nodejs npm; yum clean all

# copy source
COPY /src /src

# Install app dependencies
RUN cd /src; npm install

CMD ["node", "/src/app.js", "80"]
