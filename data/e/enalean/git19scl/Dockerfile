FROM centos:centos6

MAINTAINER Manuel VACELET, manuel.vacelet@enalean.com

RUN yum install -y rpm-build \
    help2man \
    scl-utils-build \
    asciidoc \
    xmlto \
    desktop-file-utils \
    emacs \
    expat-devel \
    gettext \
    libcurl-devel \
    pcre-devel \
    openssl-devel \
    zlib-devel \
    'perl(Error)' \
    'perl(ExtUtils::MakeMaker)' \
    gcc \
    wget && \
    yum clean all

RUN rpm --import 'https://www.redhat.com/security/fd431d51.txt'

RUN useradd builder

USER builder
WORKDIR /home/builder
RUN wget http://ftp.redhat.com/pub/redhat/linux/enterprise/6Server/en/RHSCL/SRPMS/git19-1.2-4.el6.src.rpm && rpm -K git19-1.2-4.el6.src.rpm
RUN wget http://ftp.redhat.com/pub/redhat/linux/enterprise/6Server/en/RHSCL/SRPMS/git19-git-1.9.4-4.el6.1.src.rpm && rpm -K git19-git-1.9.4-4.el6.1.src.rpm

RUN rpmbuild --rebuild git19-1.2-4.el6.src.rpm

USER root
RUN yum localinstall -y /home/builder/rpmbuild/RPMS/x86_64/git19-runtime-1.2-4.el6.x86_64.rpm /home/builder/rpmbuild/RPMS/x86_64/git19-build-1.2-4.el6.x86_64.rpm

RUN yum install -y tar

USER builder
WORKDIR /home/builder
RUN rpmbuild --rebuild git19-git-1.9.4-4.el6.1.src.rpm
