# Dockerfile with Spack and OpenMPI

FROM rezzonic/spack
MAINTAINER rezzonic

RUN $SPACK_ROOT/bin/spack install openmpi schedulers=slurm
RUN /bin/bash -c "source /spack/share/spack/setup-env.sh"
