FROM centos:7
RUN yum install -y epel-release
RUN yum install -y rpm-build redhat-rpm-config autoconf zlib-devel libselinux-devel libuuid-devel apr-devel apr-util-devel pcre-devel openldap-devel lua-devel libxml2-devel distcache-devel openssl-devel automake libtool make doxygen db4-devel postgresql-devel mysql-devel sqlite-devel freetds-devel unixODBC-devel nss-devel libdb4-devel freetds-devel cmake gcc-c++ fakeroot
RUN yum -y update && yum clean all
