###   Start by creating a "builder"   ###
# We'll compile all needed packages in the builder, and then
# we'll just get only what we need for the actual APP

ARG ANTs_VERSION=v2.3.1
ARG DEBIAN_VERSION=10.2-slim

FROM debian:${DEBIAN_VERSION}

## install libraries needed to build ANTs:
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    git-core \
    cmake \
    g++ \
    zlib1g-dev \
  && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y

# Specify where to install packages:
ENV ANTS_FOLDER=/usr/local/ANTs

###   Install ANTs   ###
# The following installs a given version of ANTs:

# Grab the Github repository, checkout the needed version,
#   build
ARG ANTs_VERSION
RUN cd /tmp && \
    git clone https://github.com/ANTsX/ANTs.git && \
    cd ANTs && \
    git checkout ${ANTs_VERSION} && \
    buildDir=${PWD}/build && \
    mkdir -p $buildDir ${ANTS_FOLDER} && \
    cd $buildDir && \
    cmake \
        -DCMAKE_INSTALL_PREFIX=${ANTS_FOLDER} \
        -DBUILD_SHARED_LIBS=OFF \
	-DSuperBuild_ANTS_USE_GIT_PROTOCOL=OFF \
        -DBUILD_TESTING=OFF \
        -DRUN_LONG_TESTS=OFF \
        -DRUN_SHORT_TESTS=OFF \
        /tmp/ANTs 2>&1 | tee cmake.log && \
    make 2>&1 | tee build.log && \
    cd ${buildDir}/ANTS-build && \
    make install 2>&1 | tee install.log && \
    rm -r /tmp/ANTs

# Add ANTs/bin to the path:
ENV PATH=$ANTS_FOLDER/bin/:$PATH


