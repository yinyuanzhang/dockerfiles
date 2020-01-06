FROM debian:jessie
MAINTAINER David Personette <dperson@dperson.com>

# Install openvpn
RUN export DEBIAN_FRONTEND='noninteractive' && \
    apt-get update -qq && \
    apt-get install -qqy --no-install-recommends iptables openvpn nano openssh-server htop traceroute\
                $(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}') &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    addgroup --system vpn
    
RUN useradd dummy_ssh

RUN echo 'dummy_ssh:dummy' | chpasswd

RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

COPY openvpn.sh /usr/bin/

VOLUME ["/run", "/tmp", "/var/cache", "/var/lib", "/var/log", "/var/tmp", \
            "/vpn"]

EXPOSE 22

ENTRYPOINT ["openvpn.sh"]
