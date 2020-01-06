FROM fedora
RUN dnf update -y && \
    dnf install -y man which vim htop iputils iproute telnet tcpdump dstat bind-utils ldns-utils net-tools nc6 openssh-clients findutils httpie jq ack awscli python-pip && \
    pip install requests requests_unixsocket

