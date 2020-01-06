FROM adoptopenjdk/openjdk8-openj9:alpine-slim

LABEL de.kdac.bitbucket.maintainer = "Claus Böhmer" \
      de.kdac.bitbucket.authors = "eso@bistum-eichstaett.de" \
      de.kdac.bitbucket.url = "https://hub.docker.com/r/kidac/bitbucket" \
      de.kdac.bitbucket.documentation = "https://hub.docker.com/r/kidac/bitbucket" \
      de.kdac.bitbucket.source = "https://github.com/kidac/bitbucket" \
      de.kdac.bitbucket.version = "6.8.0" \
      de.kdac.bitbucket.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.bitbucket.licenses = "https://www.atlassian.com/legal/software-license-agreement, https://www.atlassian.com/legal/privacy-policy" \
      de.kdac.bitbucket.title = "Atlassian Bitbucket (KDAC Version)" \
      de.kdac.bitbucket.description = "Adapted Atlassians Bitbucket Dockerfile used by https://ews.kdac.de"

ENV RUN_USER=daemon \
    RUN_GROUP=daemon \
    BITBUCKET_HOME=/var/atlassian/application-data/bitbucket \
    BITBUCKET_INSTALL_DIR=/opt/atlassian/bitbucket \
    LD_LIBRARY_PATH=/usr/lib

VOLUME ["${BITBUCKET_HOME}"]

EXPOSE 7990 7999

WORKDIR $BITBUCKET_HOME

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]

RUN apk --no-cache upgrade \
 && apk add --no-cache bash curl ghostscript motif ttf-dejavu tini git git-daemon \
 && fc-cache -f

COPY entrypoint.sh /entrypoint.sh

ARG BITBUCKET_VERSION=6.8.0
ARG DOWNLOAD_URL=https://www.atlassian.com/software/stash/downloads/binary/atlassian-bitbucket-${BITBUCKET_VERSION}.tar.gz

RUN mkdir -p ${BITBUCKET_INSTALL_DIR} \
 && curl -jkSL ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "$BITBUCKET_INSTALL_DIR" \
 && chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL_DIR}/ \
 && ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
 && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 \
 && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1
