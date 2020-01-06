
FROM quay.io/biocontainers/abyss:2.1.1--h02d93b8_0
MAINTAINER olga.botvinnik@czbiohub.org

# Add an OpenMPI file specifying that there are two slots per node (for AWS)
COPY openmpi-hostfile-aws /usr/local/etc/
RUN ls -lha /usr/local/etc/openmpi*

# Change to "main" so that openmpi doesn't complain about running as root
# Add user "main" because that's what is expected by this image
RUN useradd -ms /bin/bash main
USER main
