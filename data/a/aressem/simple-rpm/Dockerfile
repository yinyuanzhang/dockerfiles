FROM centos:7

# Needed to run vespa
RUN yum-config-manager --add-repo https://copr.fedorainfracloud.org/coprs/g/vespa/vespa/repo/epel-7/group_vespa-vespa-epel-7.repo && \
    yum -y install epel-release && \
    yum -y install centos-release-scl && \
    yum -y --enablerepo=epel-testing install \
                   Judy \
                   lz4 \
                   zlib \
                   libicu \
                   llvm3.9 \
                   java-1.8.0-openjdk \
                   openssl \
                   perl \
                   perl-Env \
                   perl-JSON \
                   perl-IO-Socket-IP \
                   libatomic \
                   net-tools \
                   less \
                   vespa-boost \
                   vespa-libtorrent \
                   vespa-zookeeper-c-client \
                   vespa-cppunit 


