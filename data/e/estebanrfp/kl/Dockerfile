FROM kalilinux/kali-linux-docker:latest

RUN apt update -y \
    && apt full-upgrade -y \
    && apt dist-upgrade -y \
    && apt autoremove -y \
    && apt clean -y \
    && apt autoclean -y \
    && apt install python htop net-tools openssl nmap metasploit-framework -y
