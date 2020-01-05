# For security, we use kubernetes community maintained debian base image.
# https://github.com/kubernetes/kubernetes/blob/master/build/debian-base/
FROM k8s.gcr.io/debian-base:v1.0.0

# Keep packages up to date and install packages for our needs.
RUN apt-get update \
    && apt-get upgrade -y \
    && clean-install \
    util-linux \
    e2fsprogs \
    bash \
    fio \
    iproute2 \
    strace \
    dnsutils \
    procps \
    netcat \
    telnet

ADD init.bashrc /etc/profile.d/

CMD ["/bin/bash"]
