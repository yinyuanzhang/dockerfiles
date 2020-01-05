FROM unifem/coupler-desktop:latest
LABEL maintainer "Jim Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

ARG BB_TOKEN

ADD image $DOCKER_HOME/

# install meshio
RUN apt-get update && \
    pip3 install -U meshio

# Checkout and install PyOverture
RUN git clone --depth=1 https://${BB_TOKEN}@bitbucket.org/qiaoc/pyovcg.git 2> /dev/null && \
    cd pyovcg && \
    perl -e 's/https:\/\/[\w:\.]+@([\w\.]+)\//git\@$1:/' -p -i .git/config && \
    python3 setup.py install && \
    cd .. && rm -rf pyovcg


# Check out and install pydtk2
# make sure to add env CC=mpicxx
RUN git clone --depth=1 https://${BB_TOKEN}@bitbucket.org/qiaoc/pydtk2.git 2> /dev/null && \
    cd pydtk2 && \
    perl -e 's/https:\/\/[\w:\.]+@([\w\.]+)\//git\@$1:/' -p -i .git/config && \
    env CC=mpicxx python3 setup.py install && \
    cd .. && rm -rf pydtk2

# Check out and install fem solver
RUN git clone --depth=1 https://${BB_TOKEN}@bitbucket.org/qiaoc/fesol.git 2> /dev/null && \
    cd fesol && \
    perl -e 's/https:\/\/[\w:\.]+@([\w\.]+)\//git\@$1:/' -p -i .git/config && \
    python3 setup.py install && \
    cd .. && rm -rf fesol

# lbcalculix and pyccx
RUN git clone --depth=1 https://${BB_TOKEN}@bitbucket.org/qiaoc/libcalculix.git 2> /dev/null && \
    cd libcalculix && \
    make && \
    make install && \
    \
    git clone --depth=1 https://${BB_TOKEN}@bitbucket.org/qiaoc/pyccx.git 2> /dev/null && \
    cd pyccx && \
    python3 setup.py install && \
    \
    rm -rf /tmp/*

USER root
WORKDIR $DOCKER_HOME

RUN chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME
