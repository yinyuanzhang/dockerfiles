FROM ligo/software:el7

LABEL name="LIGO RPM Test - Testing" \
      maintainer="Adam Mercer <adam.mercer@ligo.org>" \
      date="20190129" \
      support="Reference Platform"

# initialise metadata
RUN yum makecache

# install ldg-client
RUN yum -y install ldg-client

# enable production-staging and testing repositories
RUN yum -y install lscsoft-production-staging-config \
      lscsoft-testing-config

# install any updates and clear cache
RUN yum clean all && \
      yum makecache && \
      yum -y update && \
      yum clean all
