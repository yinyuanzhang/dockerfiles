FROM centos:7
MAINTAINER Stefan Schueffler <s.schueffler@softgarden.de>

RUN    set -x \
    && yum -y install epel-release \
    && yum -y update \
    && yum -y install exim \
    && yum clean all

EXPOSE 25 465 587

ENTRYPOINT ["exim"]
CMD ["-bd", "-v"]

