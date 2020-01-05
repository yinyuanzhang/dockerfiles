FROM centos:centos7

RUN mkdir -p /etc/grid-security/certificates /etc/grid-security/vomsdir /etc/grid-security/xrd /stash //stashcache-cache-server

RUN yum -y update

RUN yum -y install curl \
                   gperftools \
                   hostname 

RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

RUN yum -y install http://repo.opensciencegrid.org/osg/3.4/osg-3.4-el7-release-latest.rpm

RUN yum clean all --enablerepo=*

RUN yum -y install epel-release \
                   yum-plugin-priorities \
                   redhat-lsb-core \
                   osg-ca-certs \
                   stashcache-daemon \
                   fetch-crl \
                   stashcache-cache-server

RUN rpm -qa | grep xrootd

COPY stashcache_config.cfg /etc/xrootd/xrootd-stashcache-cache-server.cfg

COPY stashcache-robots.txt /etc/xrootd/stashcache-robots.txt
COPY Authfile-noauth /etc/xrootd/Authfile-noauth
RUN chown -R xrootd:xrootd /stash
RUN chown -R xrootd:xrootd /etc/xrootd

COPY run_stashcache.sh /
RUN chmod 775 /run_stashcache.sh
CMD ["/run_stashcache.sh"]

# COPY run_condor.sh /
# RUN chmod 775 /run_condor.sh
# CMD ["/run_condor.sh"]
