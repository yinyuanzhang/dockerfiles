FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
        msmtp \
        tcl \
        tcllib \
        libusb-1.0-0-dev \
        supervisor \
#        unzip \
#        rsyslog \
        --no-install-recommends && \
        rm -rf /var/lib/apt/lists/*
COPY HMserver /
COPY firmware/ /firmware/
COPY /packages/lighttpd/ /
COPY X86_32_Debian_Wheezy/packages-eQ-3/HS485D/ /
COPY X86_32_Debian_Wheezy/packages-eQ-3/RFD/ /
COPY X86_32_Debian_Wheezy/packages-eQ-3/WebUI/ /
COPY X86_32_Debian_Wheezy/packages-eQ-3/LinuxBasis/ /
COPY WebUI/ /
COPY HMserver/ /
RUN ln -s / /opt/hm && \
    rm -rf /usr/local/* && \
    mkdir -p /usr/local/etc && \
    mv /etc/config /usr/local/etc/ && \
    ln -s /usr/local/etc/config /etc/config
COPY docker/supervisor/ /etc/supervisor/
COPY docker/VERSION /boot/
COPY docker/reboot /sbin/

VOLUME ["/usr/local"] 

EXPOSE 80 90 443 2000 2001 2002 8001 8002 8181 4430 4431 4432 44381

CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
