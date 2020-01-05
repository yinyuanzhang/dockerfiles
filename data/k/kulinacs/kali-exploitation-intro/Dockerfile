FROM kalilinux/kali-linux-docker:latest

RUN apt-get update && apt-get install -y \
    grc \
    nmap && \
    rm -rf /var/lib/apt/lists/*

COPY .bashrc /root/.bashrc

ENTRYPOINT "/bin/bash"
