FROM bitnami/minideb:unstable

# install debos build dependencies
RUN install_packages \
    golang \
    git \
    build-essential \
    ca-certificates \
    libglib2.0-dev \
    libostree-dev \
    # fakemachine runtime dependencies
    qemu-system-x86 \
    qemu-user-static \
    debootstrap \
    busybox \
    systemd-container \
    linux-image-amd64 \
    binfmt-support
    
ENV GOPATH=/opt/
RUN go get -u github.com/go-debos/debos/cmd/debos

ENV PATH="/opt/bin/:${PATH}"
WORKDIR /root
