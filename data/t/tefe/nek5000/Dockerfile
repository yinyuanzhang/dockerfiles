FROM ubuntu:bionic
MAINTAINER "Thomas Enzinger <info@thomas-enzinger.de>"

# install software
RUN apt-get update &&  apt-get install -f -y                                                \
      sudo curl wget curl git                                                               \
      nano vim                                                                              \
      build-essential cmake gfortran gcc                                                    \
      libopenmpi-dev openmpi-bin libcr-dev mpich                                            \
      libcgal-dev                                                                           \
      bash bash-completion libboost-all-dev software-properties-common                      \
      libx11-dev mesa-common-dev libglu1-mesa-dev libxrandr-dev libxi-dev libxt-dev         \
 && rm -rf /var/lib/apt/lists/*

# config os
ENV IMAGE_USER_NAME=tefe
ENV IMAGE_SRC_DIR=/opt/nek5000
ENV NEK_SOURCE_ROOT="${IMAGE_SRC_DIR}"
ENV SOURCE_ROOT="${NEK_SOURCE_ROOT}"

RUN addgroup "${IMAGE_USER_NAME}" && useradd -m --shell /bin/bash -g "${IMAGE_USER_NAME}" "${IMAGE_USER_NAME}"   \
 && echo "${IMAGE_USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers                                             \
 && echo 127.0.1.1 $(hostname) >> /etc/hosts

SHELL ["/bin/bash", "-c"]

ENV CC=/usr/bin/mpicc
ENV CXX=/usr/bin/mpic++
ENV FC=/usr/bin/gfortran
ENV CFLAGS="-I/usr/include/mpi -I${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib/build/include"
ENV LDFLAGS=""

ENV CMAKE_C_COMPILER=${CC}
ENV CMAKE_CXX_COMPILER=${CXX}

ENV GSLIBPATH="${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib"

ARG SOURCE_COMMIT
ARG VERSION
ARG NEK5000_GIT_URL
ARG NEK5000_GIT_HASH
ARG NEK5000_GIT_BRANCH

#
COPY scripts/* /opt/
RUN /opt/load_src && rm -f /opt/load_src                                                                \
 && echo "export PATH=$PATH:${IMAGE_SRC_DIR}/bin:${NEK_SOURCE_ROOT}/3rd_party/parMETIS/bin" >> /root/.bashrc                                      \
 && echo "export PATH=$PATH:${IMAGE_SRC_DIR}/bin:${NEK_SOURCE_ROOT}/3rd_party/parMETIS/bin" >> "/home/${IMAGE_USER_NAME}/.bashrc"                 \
 && echo "export OMPI_MCA_btl_vader_single_copy_mechanism=none" >> /root/.bashrc                        \
 && echo "export OMPI_MCA_btl_vader_single_copy_mechanism=none" >> "/home/${IMAGE_USER_NAME}/.bashrc"   \
 && echo "export NEK_SOURCE_ROOT=${NEK_SOURCE_ROOT}" >> /root/.bashrc \
 && echo "export NEK_SOURCE_ROOT=${NEK_SOURCE_ROOT}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export SOURCE_ROOT=${SOURCE_ROOT}" >> /root/.bashrc \
 && echo "export SOURCE_ROOT=${SOURCE_ROOT}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export CC=${CC}" >> /root/.bashrc \
 && echo "export CC=${CC}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export CXX=${CXX}" >> /root/.bashrc \
 && echo "export CXX=${CXX}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export FC=${FC}" >> /root/.bashrc \
 && echo "export FC=${FC}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export CLFLAGS='${CFLAGS} -I${NEK_SOURCE_ROOT}/3rd_party/blasLapack -I${NEK_SOURCE_ROOT}/3rd_party/cvode/include -I${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib/build/include -I${NEK_SOURCE_ROOT}/3rd_party/hypre/include -I${NEK_SOURCE_ROOT}/3rd_party/parMETIS/include -I${NEK_SOURCE_ROOT}/3rd_party/parRSB/parRSB/build/include'" >> /root/.bashrc \
 && echo "export CLFLAGS='${CFLAGS} -I${NEK_SOURCE_ROOT}/3rd_party/blasLapack -I${NEK_SOURCE_ROOT}/3rd_party/cvode/include -I${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib/build/include -I${NEK_SOURCE_ROOT}/3rd_party/hypre/include -I${NEK_SOURCE_ROOT}/3rd_party/parMETIS/include -I${NEK_SOURCE_ROOT}/3rd_party/parRSB/parRSB/build/include'" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export LDFLAGS='${LDFLAGS} -L${NEK_SOURCE_ROOT}/3rd_party/blasLapack -L${NEK_SOURCE_ROOT}/3rd_party/cvode/lib -L${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib/build/lib -L${NEK_SOURCE_ROOT}/3rd_party/hypre/lib -L${NEK_SOURCE_ROOT}/3rd_party/parMETIS/lib -L${NEK_SOURCE_ROOT}/3rd_party/parRSB/parRSB/build/lib'" >> /root/.bashrc \
 && echo "export LDFLAGS='${LDFLAGS} -L${NEK_SOURCE_ROOT}/3rd_party/blasLapack -L${NEK_SOURCE_ROOT}/3rd_party/cvode/lib -L${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib/build/lib  -L${NEK_SOURCE_ROOT}/3rd_party/hypre/lib -L${NEK_SOURCE_ROOT}/3rd_party/parMETIS/lib -L${NEK_SOURCE_ROOT}/3rd_party/parRSB/parRSB/build/lib'" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export CMAKE_C_COMPILER=${CC}" >> /root/.bashrc \
 && echo "export CMAKE_C_COMPILER=${CC}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export CMAKE_CXX_COMPILER=${CXX}" >> /root/.bashrc \
 && echo "export CMAKE_CXX_COMPILER=${CXX}" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && echo "export GSLIBPATH=${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib" >> /root/.bashrc \
 && echo "export GSLIBPATH=${NEK_SOURCE_ROOT}/3rd_party/gslib/gslib" >> /home/${IMAGE_USER_NAME}/.bashrc \
 && source /root/.bashrc

WORKDIR "${NEK_SOURCE_ROOT}"
RUN /opt/install && rm -f /opt/install

#
VOLUME ["${NEK_SOURCE_ROOT}/run"]
WORKDIR "${NEK_SOURCE_ROOT}/run"
USER "${IMAGE_USER_NAME}"

#
ENTRYPOINT ["/bin/bash", "-ci"]

