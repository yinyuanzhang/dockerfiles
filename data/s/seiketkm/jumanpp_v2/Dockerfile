FROM amazonlinux:2.0.20190508 as build-env
ARG JUMANPP_FILENAME=jumanpp-2.0.0-rc2.tar.xz
ARG TARGET_DIR=/var/task
RUN yum -y update && yum -y install \
    wget &&\
    yum groupinstall "Development Tools" -y &&\
    yum clean all &&\
    wget https://cmake.org/files/v3.10/cmake-3.10.0.tar.gz &&\
    tar -xvzf cmake-3.10.0.tar.gz &&\
    cd /cmake-3.10.0 &&\
    ./bootstrap &&\
    make install &&\
    cd /
RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc2/${JUMANPP_FILENAME} &&\
    tar xf /${JUMANPP_FILENAME}
RUN mkdir -p ${TARGET_DIR} &&\
    cd ${TARGET_DIR} &&\
    cmake /jumanpp-2.0.0-rc2 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${TARGET_DIR} &&\
    make install -j4

FROM amazonlinux:2.0.20190508 as run-env
ARG TARGET_DIR=/var/task
COPY --from=build-env ${TARGET_DIR}/bin/jumanpp \
    ${TARGET_DIR}/bin/jumanpp
COPY --from=build-env ${TARGET_DIR}/libexec/jumanpp/jumandic.config \
    ${TARGET_DIR}/libexec/jumanpp/jumandic.config
COPY --from=build-env ${TARGET_DIR}/libexec/jumanpp/jumandic.jppmdl \
    ${TARGET_DIR}/libexec/jumanpp/jumandic.jppmdl

ENTRYPOINT ["/bin/bash"]
