FROM antik486/centos71
MAINTAINER bekberov <bekberovkerim@gmail.com>

RUN yum -y update && \
    yum -y install \
           tar \
           gcc \
           glibc-devel \
           make \
           ncurses-devel \
           openssl-devel \
           autoconf \
           curl \
           git   && \
           yum clean all

RUN curl -O https://raw.githubusercontent.com/spawngrid/kerl/master/kerl && \
    chmod a+x kerl && \
    mv kerl /usr/bin && \
    kerl update releases && \
    KERL_CONFIGURE_OPTIONS=--enable-hipe kerl build 18.2.1 r18 && \
    kerl install r18 /opt/erl && \
    kerl cleanup all && \
    rm -f .kerl/archives/*.tar.gz && \
    ln -s /opt/erl /usr/lib/erlang

ENV PATH /usr/lib/erlang/bin:$PATH

VOLUME ["/opt/app"]

WORKDIR /opt/app
