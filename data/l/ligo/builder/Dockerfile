FROM ligo/base:el7

RUN yum -y groupinstall 'Development Tools' && \
    yum install -y \
      ccache \
      clang && \
    yum clean all
