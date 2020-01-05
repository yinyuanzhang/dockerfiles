FROM binhnv/hadoop-eco:1.0
LABEL maintainer="Binh Van Nguyen<binhnv80@gmail.com>"

ENV NIFI_VERSION=1.5.0 \
    NIFI_HOME="${MY_APP_DIR}/nifi"
ENV NIFI_BIN_URL="http://archive.apache.org/dist/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz"

WORKDIR ${NIFI_HOME}
RUN mkdir -p ${NIFI_HOME} \
    && curl -sL ${NIFI_BIN_URL} | tar -xz -C ${NIFI_HOME} --strip-component=1 \
    # NiFi use /bin/sh as the shell to run and on Ubuntu this shell
    # is linked to dash which doesn't have source command. nifi.sh command
    # use this function
    && ln -sf bash /bin/sh

COPY files/share/services ${MY_SERVICE_DIR}/

