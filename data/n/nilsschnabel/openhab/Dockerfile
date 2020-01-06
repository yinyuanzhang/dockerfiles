FROM openhab/openhab:2.4.0-armhf-debian

ENV QEMU_EXECVE 1
COPY . /usr/bin
RUN [ "qemu-arm-static", "/bin/sh", "-c", "ln -s resin-xbuild /usr/bin/cross-build-start; ln -s resin-xbuild /usr/bin/cross-build-end; mv /bin/sh /bin/sh.real; ln -s /bin/sh.real /bin/sh" ]

RUN [ "cross-build-start" ]

# Install additional packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        iputils-arping \
        openssh-client \
        android-tools-adb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN [ "cross-build-end" ]
