FROM jenkins/jenkins:alpine
USER root

# set version label
LABEL maintainer="Nightah"

# package versions
ARG NOTARY_VER="0.6.1"

# Install the latest Docker CE binaries
RUN \
echo "**** install runtime packages ****" && \
apk add --no-cache \
    docker && \
curl -o \
/usr/bin/notary -L \
    "https://github.com/theupdateframework/notary/releases/download/v${NOTARY_VER}/notary-Linux-amd64" && \
chmod +x /usr/bin/notary && \
echo "**** cleanup ****" && \
rm -rf \
    /tmp/*

# set default user
USER jenkins