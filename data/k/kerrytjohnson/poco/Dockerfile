FROM centos:centos7.5.1804

ENV POCO_VER=1.9.4
ENV POCO_URL=https://github.com/pocoproject/poco/archive
ENV POCO_SRC_FILE=poco-${POCO_VER}-release.tar.gz
ENV POCO_ARTIFACT=poco-${POCO_VER}.tgz

RUN yum -y -q install   gcc-c++         \
                        make            \
                        openssl         \
                        openssl-devel   \
                        wget

VOLUME /var/tmp

WORKDIR /tmp
RUN wget --quiet ${POCO_URL}/${POCO_SRC_FILE}   \
    && tar xzf ${POCO_SRC_FILE}
    
# Deliberately create a new layer for the build step
WORKDIR /tmp/poco-poco-${POCO_VER}-release
RUN ./configure     \
    && make -s

# Deliberately create a new layer for the installation step
RUN make install        \
    && rm -rf /tmp/*
    
WORKDIR /usr/local
RUN tar czf /tmp/${POCO_ARTIFACT} ./include ./lib ./bin

CMD cp /tmp/${POCO_ARTIFACT} /var/tmp/
