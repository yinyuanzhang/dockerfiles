FROM vassoz/sdr-balena-raspberry-pi2-build

MAINTAINER Vasyl Petrushko <vassoz@gmail.com>

RUN [ "cross-build-start" ]

RUN echo 'blacklist dvb_usb_rtl28xxu' > /etc/modprobe.d/raspi-blacklist.conf

WORKDIR /tmp

RUN git clone git://git.osmocom.org/rtl-sdr.git && \
    mkdir rtl-sdr/build && \
    cd rtl-sdr/build && \
    cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON && \
    make && \
    make install && \
    ldconfig && \
    rm -rf /tmp/rtl-sdr

ENV LD_LIBRARY_PATH=/usr/local/lib

RUN [ "cross-build-end" ]
