##################################
#            Builder             #
##################################
FROM alpine AS builder

# --------------------
# -      CONFIG      -
# --------------------
ENV IESI_VERSION v0.1.0

RUN wget -O iesi.tar.gz https://github.com/metadew/iesi/releases/download/${IESI_VERSION}/iesi-dist-${IESI_VERSION}.tar.gz
RUN tar -xzf iesi.tar.gz
RUN mv ${IESI_VERSION}/ iesi/

##################################
#    MINIMAL RESULT CONTAINER    #
##################################
FROM openjdk:8-jre-slim

# --------------------
# -      CONFIG      -
# --------------------
ENV IESI_HOME /home/iesi

# Get IESI from builder stage
COPY --from=builder /iesi ${IESI_HOME}

# Move SQLite repo to volume
RUN sed -E 's|(.*iesi.metadata.repository.sqlite.file=#iesi.home#)(/repository.db3)|\1/repo\2|' -i ${IESI_HOME}/conf/iesi-repository.conf

# Set working dir
WORKDIR ${IESI_HOME}/bin

# Set volumes
VOLUME ["${IESI_HOME}/bin/metadata/in", "${IESI_HOME}/bin/metadata/out", "${IESI_HOME}/repo"]
