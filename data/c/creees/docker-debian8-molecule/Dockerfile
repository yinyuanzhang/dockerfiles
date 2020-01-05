FROM debian:jessie
LABEL maintainer="Chris Bermudez"

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       sudo \
       build-essential libffi-dev libssl-dev \
       python-pip python-dev \
       iproute iproute2 \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

VOLUME ["/sys/fs/cgroup"]
CMD ["/lib/systemd/systemd"]
