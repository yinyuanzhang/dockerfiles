#use centos base image
FROM centos:centos7.6.1810

#install packages needed by MAKLicenseManager
RUN yum install -y glibc.i686
RUN yum install -y redhat-lsb
RUN yum install -y wget

# prepare installation directory
RUN mkdir /app
WORKDIR /app

#make sure we run as non root
RUN adduser maintainer
RUN chown maintainer:users /app
USER maintainer

# download MAKLicenseManager
RUN wget http://ftp.mak.com/out/MAKLicenseManager-linux64-setup.tar.gz
RUN tar -xvf MAKLicenseManager-linux64-setup.tar.gz

#ports needed for MAKLicenseManager
EXPOSE 2080
EXPOSE 27000-27009

#start MAKLicenseManager
CMD /app/LicenseManager/lmgrd -z
