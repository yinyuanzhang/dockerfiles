FROM ubuntu:15.10

ENV v_rar2fs=${RAR2FS_VERSION:-1.22.0}
ENV v_unrar=${UNRAR_VERSION:-5.3.1}
ENV dir_source=${SOURCE:-/media}
ENV dir_target=${TARGET:-/rar2fs}

RUN WORKDIR=`mktemp -d` && \
    cd $WORKDIR && \

    # Get deps
    apt-get update && \
    apt-get -y install \
      wget \
      make \
      libfuse-dev \
      g++ && \

    # Get, make and install unrar
    wget http://www.rarlab.com/rar/unrarsrc-${v_unrar}.tar.gz && \
    tar zxvf unrarsrc-${v_unrar}.tar.gz && \
    cd unrar && \
    make && \
    make install && \
    make lib && \
    make install-lib && \
    cd .. && \

    # Get, make and install rar2fs
    wget https://github.com/hasse69/rar2fs/releases/download/v${v_rar2fs}/rar2fs-${v_rar2fs}.tar.gz -O rar2fs-${v_rar2fs}.tar.gz && \
    tar zxvf rar2fs-${v_rar2fs}.tar.gz && \
    cd rar2fs-${v_rar2fs} && \
    ./configure --with-unrar=../unrar --with-unrar-lib=/usr/lib/ && \
    make && \
    make install && \

    # Cleanup
    rm -rf $WORKDIR

VOLUME ["$dir_source", "$dir_target"]

# mount
CMD /usr/local/bin/rar2fs $dir_source $dir_target && \

    # make this into a deamon
    # see: "Starting a long-running worker process"
    # https://docs.docker.com/engine/quickstart/
    while true; do echo DEAMON; sleep 1; done

## doc
## thanks to: https://github.com/docker/docker/issues/9448#issuecomment-65529399
# docker build .
# get the image id
# docker run -d -it --privileged --cap-add SYS_ADMIN --device /dev/fuse -v "$PWD/source":/media --name rar2fs <image id>
