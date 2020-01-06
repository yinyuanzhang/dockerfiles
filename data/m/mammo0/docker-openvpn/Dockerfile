# needed for cross building
FROM mammo0/armv7hf-debian-qemu AS armBin


# Original credit: https://github.com/jpetazzo/dockvpn

# Smallest base image
FROM arm32v6/alpine:latest

LABEL maintainer="Kyle Manna <kyle@kylemanna.com>"
LABEL maintainer="Marc Ammon <marc.ammon@fau.de>"

# start cross building
COPY --from=armBin /usr/bin/cross-build-start /usr/bin/
COPY --from=armBin /usr/bin/cross-build-end /usr/bin/
COPY --from=armBin /usr/bin/qemu-arm-static /usr/bin/
COPY --from=armBin /usr/bin/resin-xbuild /usr/bin/
RUN [ "cross-build-start" ]
# Testing: pamtester
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update openvpn iptables bash easy-rsa openvpn-auth-pam google-authenticator pamtester && \
    ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

# Needed by scripts
ENV OPENVPN /etc/openvpn
ENV EASYRSA /usr/share/easy-rsa
ENV EASYRSA_PKI $OPENVPN/pki
ENV EASYRSA_VARS_FILE $OPENVPN/vars

# Prevents refused client connection because of an expired CRL
ENV EASYRSA_CRL_DAYS 3650

VOLUME ["/etc/openvpn"]

# Internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`
EXPOSE 1194/udp

CMD ["ovpn_run"]

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

# end cross building
RUN [ "cross-build-end" ]

# Add support for OTP authentication using a PAM module
ADD ./otp/openvpn /etc/pam.d/
