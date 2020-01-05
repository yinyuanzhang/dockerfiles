FROM centos:7

MAINTAINER "Claire Bertelli" <claire.bertelli@gmail.com>

ADD http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz /apps/

RUN yum -y install http://mirror.its.sfu.ca/mirror/CentOS-Third-Party/epel/epel-release-latest-7.noarch.rpm \
  && yum -y upgrade \
  && yum -y install gcc git\
  && yum -y install perl perl-App-cpanminus perl-Data-Dumper perl-Log-Log4perl perl-Moose perl-Config-Simple \
  && cpanm --force TAP::Harness::Env \
  && cpanm MooseX::Singleton Bio::Perl \
  && cd /apps/ \
  && tar -zxf hmmer-3.1b2-linux-intel-x86_64.tar.gz \
  && cd /apps/hmmer-3.1b2-linux-intel-x86_64 \
  && ./configure \
  && make \
  && make check \
  && make install \
  && ln -S /apps/hmmscan /apps/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmscan \
  && yum -y remove gcc \
  && yum clean all

RUN git clone https://github.com/brinkmanlab/islandpath.git /apps/islandpath

#VOLUME [ "/data" ]
 
ENTRYPOINT []
CMD ["/apps/islandpath/Dimob.pl"]


