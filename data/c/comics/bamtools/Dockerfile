FROM comics/centos
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>

##############################################################
# Software:             bamtools
# Software Version:     2.5.1
# Software Website:     https://github.com/pezmaster31/bamtools
# Description:          C++ API & command-line toolkit for working with BAM data
##############################################################

ENV APP_NAME=bamtools
ENV VERSION=v2.5.1
ENV GIT=https://github.com/pezmaster31/bamtools.git
ENV DEST=/software/applications/$APP_NAME
ENV PATH=$DEST/$VERSION/bin:$PATH
ENV CPATH=$DEST/$VERSION/include/bamtools:$CPATH
ENV LPATH=$DEST/$VERSION/lib64:$LPATH
ENV LIBRARY_PATH=$DEST/$VERSION/lib64:$LIBRARY_PATH

RUN yum install -y \
       cmake3 \
       zlib-devel && \
    yum clean all && \
    rm -rf /var/cache/yum ; 
RUN git clone $GIT && \
    cd $APP_NAME && \
    git checkout tags/$VERSION && \
    mkdir -p /usr/share/licenses/$APP_NAME-$VERSION && \
    cp LICENSE /usr/share/licenses/$APP_NAME-$VERSION/ && \
    mkdir build && \
    cd build && \
    cmake3 -DCMAKE_INSTALL_PREFIX:PATH=$DEST/$VERSION .. && \
    make && \
    make install && \
    cd ../.. &&  \
    rm -rf $APP_NAME
CMD ["/bin/bash"]

