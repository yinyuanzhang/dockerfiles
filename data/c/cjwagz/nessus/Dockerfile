FROM centos:7
MAINTAINER cjwagz

# Download GPG and RPM
ADD https://tenable-downloads-production.s3.amazonaws.com/uploads/download/file/6979/tenable-2048.gpg /tmp
ADD https://tenable-downloads-production.s3.amazonaws.com/uploads/download/file/7857/Nessus-7.1.1-es6.x86_64.rpm /tmp

RUN rpm --import /tmp/tenable-2048.gpg
RUN rpm -iv /tmp/Nessus-7.1.1-es6.x86_64.rpm

EXPOSE 8834
CMD ["/opt/nessus/sbin/nessus-service"]