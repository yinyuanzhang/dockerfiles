FROM broadinstitute/picard:2.18.2

# install r-base
RUN apt-get update && \
    apt-get --no-install-recommends install -y --force-yes r-base && \
    apt-get clean autoclean && \
    apt-get autoremove -y

# create a /ifs and /gpfs volume for MSK users
VOLUME /ifs
VOLUME /gpfs
VOLUME /data
WORKDIR /data
