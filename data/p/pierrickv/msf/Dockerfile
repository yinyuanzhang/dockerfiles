FROM debian:stretch-slim
ARG DEBIAN_FRONTEND=noninteractive

# Based on https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers

RUN apt-get update -qq && apt-get install --assume-yes --force-yes \
      vim-tiny \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg \
      nmap \
  && curl -fsSL https://apt.metasploit.com/metasploit-framework.gpg.key | apt-key add - \
  && echo "deb https://apt.metasploit.com/ jessie main" >> /etc/apt/sources.list \
  && apt-get update -qq \
  && apt-get install metasploit-framework \
  && apt-get autoremove --assume-yes --force-yes \
      curl \
  && rm -rf /var/lib/apt/lists/*

CMD ["msfconsole"]
