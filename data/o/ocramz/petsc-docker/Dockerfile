FROM phusion/baseimage:0.9.18

MAINTAINER Marco Zocca, zocca.marco gmail

# # build-related env.variables
# ENV BUILDTYPE ""


# PETSc and SLEPc versions

ENV PETSC_VERSION=3.7.2 \
    SLEPC_VERSION=3.7.1 \
    ARCH=arch-linux2-c-debug \
    SWDIR=/opt

ENV PETSC_DIR=${SWDIR}/petsc-${PETSC_VERSION} \
    SLEPC_DIR=${SWDIR}/slepc-${SLEPC_VERSION} \
# export PETSC_ARCH=arch-linux2-c-debug
    PETSC_ARCH=${ARCH} \
    SLEPC_ARCH=${ARCH}


COPY setup.sh ${SWDIR}/
WORKDIR ${SWDIR}
RUN ./setup.sh ${PETSC_VERSION} ${SLEPC_VERSION} ${ARCH} ${SWDIR}


VOLUME $PETSC_DIR

WORKDIR /home