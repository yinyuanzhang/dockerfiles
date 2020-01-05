FROM centos:centos7

# Base install up-to-date and epel is required for many packages
RUN yum update -y && \
    yum install -y epel-release && \
    yum clean all

# Software development tools, RPM build requirements
RUN yum install -y auto{conf,make} ctags elfutils gcc{,-c++} gettext intltool libtool make patch{,utils} && \
    yum install -y redhat-rpm-config rpm-{build,sign} spectool && \
    yum install -y git yum-utils && \
    yum install -y libusbx libusbx-devel && \
    yum clean all

RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

CMD ["bash"]
