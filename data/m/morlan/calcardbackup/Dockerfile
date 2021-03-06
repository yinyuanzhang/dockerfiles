#introducing a variable to get the arch specific base image. The var is defined by --build-arg in the docker build command.
ARG IMAGE_ARCH
FROM ${IMAGE_ARCH}

# Dockerfile Maintainer
MAINTAINER Jan Wagner "waja@cyconet.org"

ARG BUILD_DATE
ARG BUILD_VERSION
ARG VCS_URL
ARG VCS_REF
ARG VCS_BRANCH
ARG QEMU_ARCH

ENV GIT_PROJECT=BernieO/calcardbackup

# See http://label-schema.org/rc1/ and https://microbadger.com/labels
LABEL org.label-schema.name="calcardbackup - ownCloud/Nextcloud backup tool" \
    org.label-schema.description="backup calendars and addressbooks from a local ownCloud/Nextcloud installation on Alpine Linux based container" \
    org.label-schema.vendor="Cyconet" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.build-date="${BUILD_DATE:-unknown}" \
    org.label-schema.version="${BUILD_VERSION:-unknown}" \
    org.label-schema.vcs-url="${VCS_URL:-unknown}" \
    org.label-schema.vcs-ref="${VCS_REF:-unknown}" \
    org.label-schema.vcs-branch="${VCS_BRANCH:-unknown}"

#the file is needed to emulate the different arches. Copying and removing the README.md is a neccessary workaround, because the qemu file is not present in the amd64 build. If there is no other file present, the COPY command will fail.
COPY README.md qemu-${QEMU_ARCH}-static* /usr/bin/ 
RUN rm -f /usr/bin/README.md
COPY ["run.sh", "/"]

RUN apk --no-cache update && apk --no-cache upgrade && \
  # Install dependencies
  apk --no-cache add --virtual build-dependencies ca-certificates tar curl jq && \
  # Create directory
  mkdir -p /opt/calcardbackup && cd /opt/calcardbackup && \
  # Download latest release
  curl -L $(curl -s https://api.github.com/repos/$GIT_PROJECT/releases/latest | jq -r ".tarball_url") | tar xz --strip=1 && \
  # Remove build deps
  apk del build-dependencies && \
  # Install needed packages
  apk add --update bash curl findutils mysql-client postgresql-client sqlite gzip && rm -rf /var/cache/apk/* && \
  # Create backup dir and make our start script executable
  mkdir /backup

VOLUME ["/backup"]

CMD ["/run.sh"]
