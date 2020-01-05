ARG DEBIAN_VERSION=stretch
FROM debian:"${DEBIAN_VERSION}"
LABEL maintainer="rmocius@gmail.com"

#
# BEGIN: DOCKER IN DOCKER SETUP
#

# Install Docker deps, some of these are already installed in the image but
# that's fine since they won't re-install and we can reuse the code below
# for another image someday.
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    lsb-release

# Add the Docker apt-repository
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg \
    | apt-key add - && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) stable"

# Install Docker
# TODO(bentheelder): the `sed` is a bit of a hack, look into alternatives.
# Why this exists: `docker service start` on debian runs a `cgroupfs_mount` method,
# We're already inside docker though so we can be sure these are already mounted.
# Trying to remount these makes for a very noisy error block in the beginning of
# the pod logs, so we just comment out the call to it... :shrug:
# TODO(benthelder): update docker version. This is pinned because of
# https://github.com/kubernetes/test-infra/issues/6187
ARG DOCKER_VERSION="17.09.1~ce-0~debian"
RUN apt-get update && \
    apt-get install -y --no-install-recommends docker-ce="${DOCKER_VERSION}" && \
    sed -i 's/cgroupfs_mount$/#cgroupfs_mount\n/' /etc/init.d/docker

# Move Docker's storage location
RUN echo 'DOCKER_OPTS="${DOCKER_OPTS} --data-root=/docker-graph"' | \
    tee --append /etc/default/docker
# NOTE this should be mounted and persisted as a volume ideally (!)
# We will make a fallback one now just in case
RUN mkdir /docker-graph
