FROM comics/centos
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>

##############################################################
# Software:             bwa
# Software Version:     0.7.17
# Software Website:     https://github.com/lh3/bwa.git
# Description:          Burrow-Wheeler Aligner for pairwise alignment between DNA sequences
##############################################################

ENV APP_NAME=bwa
ENV VERSION=v0.7.17
ENV GIT=https://github.com/lh3/bwa.git
ENV DEST=/software/applications/$APP_NAME/
ENV PATH=$DEST/$VERSION/:$DEST/$VERSION/bwakit:$PATH

COPY --from=comics/samtools:1.3.1 /software/applications/samtools /software/applications/samtools
ENV PATH=/software/applications/samtools/1.3.1/bin:/software/applications/bcftools/1.3.1/bin:$PATH

RUN yum install -y zlib-devel wget && \
    yum clean all && \
    git clone $GIT && \
    cd $APP_NAME && \
    git checkout tags/$VERSION && \
    make -j && \
    mkdir -p /usr/share/licenses/$APP_NAME-$VERSION && \
    cp COPYING /usr/share/licenses/$APP_NAME-$VERSION/ && \
    rm -rf .git && \
    cd ../ &&  \
    mkdir -p $DEST && \
    mv $APP_NAME $DEST/$VERSION
CMD ["/bin/bash"]

