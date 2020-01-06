FROM opensuse/leap

RUN zypper install -y docker docker-compose openssh

RUN systemctl enable docker

RUN systemctl enable sshd