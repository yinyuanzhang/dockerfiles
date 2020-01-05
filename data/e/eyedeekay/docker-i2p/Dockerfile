FROM debian:sid
ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV I2P_DIR /usr/share/i2p
EXPOSE 2827 7650 7654 7655 7656 7657 7658 7659 7660 7661 7662 4444 6668 8998
RUN apt-get update
RUN apt-get install -y i2p i2p-router procps
RUN sed -i 's/127\.0\.0\.1/0.0.0.0/g' ${I2P_DIR}/i2ptunnel.config && \
    sed -i 's/::1,127\.0\.0\.1/0.0.0.0/g' ${I2P_DIR}/clients.config && \
    printf "i2cp.tcp.bindAllInterfaces=true\n" >> ${I2P_DIR}/router.config && \
    printf "i2np.ipv4.firewalled=true\ni2np.ntcp.ipv6=false\n" >> ${I2P_DIR}/router.config && \
    printf "i2np.udp.ipv6=false\ni2np.upnp.enable=false\n" >> ${I2P_DIR}/router.config
USER i2psvc
CMD i2prouter console
