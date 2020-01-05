FROM centos:8
MAINTAINER Stefan Schueffler <s.schueffler@softgarden.de>

RUN    rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-8 \
    && yum -y install epel-release \
    && yum -y update \
    && yum -y install clamav-unofficial-sigs gpg \
    && yum clean all

# add default user conf
ADD user.conf /etc/clamav-unofficial-sigs/user.conf

ADD entrypoint.sh /

VOLUME ["/var/lib/clamav", "/var/lib/clamav-unofficial-sigs"]

ENTRYPOINT ["/entrypoint.sh"]
CMD []
