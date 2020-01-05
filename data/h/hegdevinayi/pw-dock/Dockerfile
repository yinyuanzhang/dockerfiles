# use Debian Linux as the base image
# TODO: the Debian image is pretty large; use Alpine instead? (discuss)
FROM    debian:latest

# maintainer, version, and any other identifiers
LABEL   version="qe-6.3:debian-atlas-mpich"
LABEL   maintainer="Vinay Hegde <vhegde@citrine.io>"

# QE version and other variables to use later, for consistency/portability
ENV     QE_VERSION "6.3"
ENV     QE_HOME "/home/qe"

# install the necessary dependencies using Debian APT
RUN     apt-get update \
        && apt-get install -y \
            wget \
            libatlas-base-dev \
            libatlas3-base \
            libfftw3-double3 \
            libfftw3-dev \
            libmpich-dev \
            make \
            python2

# create "qe" user and group for running pw.x
# -l = --no-log-init: do not lastlog and faillog user
# -m = create home directory
# -U = create a group named [user], add user to it
# -u = set UID for the user account
# -s = set the default login shell for user
RUN     ["/bin/bash", "-c", \
         "useradd -lmU -s /bin/bash -u 1001 qe"]

# use the "qe" user for running everything from here on
USER    qe
        
# set the working directory
WORKDIR "${QE_HOME}"

# get the QE source code, untar and install
# TODO: install all QE components (other than pw.x)
RUN     wget "https://github.com/QEF/q-e/releases/download/qe-${QE_VERSION}/qe-${QE_VERSION}.tar.gz" \
        && tar zxvf "qe-${QE_VERSION}.tar.gz" \
        && cd "qe-${QE_VERSION}" \
        && ./configure \
        && make pw

# add PWscf executables to system path
ENV     PATH "$PATH:/home/qe/qe-${QE_VERSION}/bin"

# use 2 processes for parallel tests
ENV     TESTCODE_NPROCS 2

# change to the run directory
RUN     mkdir -p "${QE_HOME}/rundir"
WORKDIR "${QE_HOME}/rundir"

# copy the PWscf input and pseudopotential files
COPY    --chown=qe:qe "scf.in" "${QE_HOME}/rundir"
COPY    --chown=qe:qe "Al.pbe-n-kjpaw_psl.1.0.0.UPF" "${QE_HOME}/rundir"

# (for now) copy the wrapper from the cwd and permit user-execution
COPY    --chown=qe:qe "wrapper.sh" "${QE_HOME}"
RUN     chmod u+x "${QE_HOME}/wrapper.sh"

# entrypoint(s) for the container
# TODO: add the actual Python driver here (should manage running and
# transferring data back to the host from the container)
ENTRYPOINT  ["/bin/sh", "-c", "${QE_HOME}/wrapper.sh"]

# any additional arguments for the wrapper/driver
CMD     []

