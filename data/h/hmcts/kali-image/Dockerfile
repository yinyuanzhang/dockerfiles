FROM kalilinux/kali-linux-docker

RUN apt-get update -y && apt-get upgrade -y \
  && apt-get install -y curl gnupg \
  && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ stretch main" | tee /etc/apt/sources.list.d/azure-cli.list \
  && curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && apt-get update -y \
  && apt-get install -y sslscan metasploit-framework azure-cli python \
  && rm -rf /var/lib/apt/lists/* \
  && addgroup --gid 1001 msf \
  && adduser --no-create-home --uid 1001 --gid 1001 --disabled-password --gecos "" msf \
  && mkdir -p /opt/jenkins \
  && chown msf:msf /opt/jenkins \
  && echo "msf ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers