FROM alpine:edge as rcore_builder

# Install some basic tools
RUN apk --no-cache add \
        bash \
        build-base \
        make \
        cmake \
        valgrind \
        binutils \
        tar \
        gzip \
        git \
        uncrustify \
        gdb \
        doxygen \
        graphviz
        

# Get yamlcpp and install it
ARG YAMLCPP_URL=https://github.com/jbeder/yaml-cpp.git
ARG YAMLCPP_TAG=yaml-cpp-0.6.2

RUN git clone --depth 1 --branch ${YAMLCPP_TAG} ${YAMLCPP_URL} \
    && (cd yaml-cpp; cmake -DCMAKE_INSTALL_PREFIX=${USRLOCAL} . ; make -j 8; make install) \
    && rm -rf yaml-cpp

