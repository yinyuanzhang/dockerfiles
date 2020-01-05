FROM centos:8
MAINTAINER Stefan Schueffler <s.schueffler@softgarden.de>

RUN    rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-8 \
    && yum -y install epel-release \
    && yum -y update \
    && yum -y install clamav-update clamav wget perl-Net-DNS \
    && yum clean all

ADD clamdownloader.pl /usr/local/bin/
ADD entrypoint.sh /

VOLUME ["/var/lib/clamav"]

CMD ["/entrypoint.sh"]
