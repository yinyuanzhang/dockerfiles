FROM comics/samtools
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>

##############################################################
# Software:             bowtie
# Software Version:     2.3.4.1
# Software Website:     https://github.com/BenLangmead/bowtie2
# Description:          bowtie2
##############################################################

ENV APP_NAME=bowtie2
ENV VERSION=v2.3.4.1
ENV GIT=https://github.com/BenLangmead/bowtie2.git
ENV DEST=/software/applications/$APP_NAME/
ENV PATH=$DEST/$VERSION/:$DEST/$VERSION/scripts/:$PATH

RUN yum install -y \
      perl-devel \
      tbb-devel \
      zlib-devel ; \
    yum clean all ; \
    rm -rf /var/cache/yum ; \    
    git clone $GIT ; \
    cd $APP_NAME ; \
    git checkout tags/$VERSION ; \
    sed -i "s#^prefix.*#prefix = $DEST#" Makefile ; \
    make -j ; \
    mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \
    cp LICENSE /usr/share/licenses/$APP_NAME-$VERSION/ ; \
    rm -rf .git ; \
    cd ../ ;  \
    mkdir -p $DEST ; \
    mv $APP_NAME $DEST/$VERSION
CMD ["/bin/bash"]

