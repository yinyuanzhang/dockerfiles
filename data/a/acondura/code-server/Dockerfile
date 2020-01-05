FROM ubuntu:latest

RUN apt-get update && apt-get -y upgrade

RUN apt-get update && apt-get install -y apt-utils openssl net-tools git locales sudo dumb-init vim curl wget unzip; \
  apt -y autoremove

RUN locale-gen en_US.UTF-8
# We unfortunately cannot use update-locale because docker will not use the env variables
# configured in /etc/default/locale so we need to set it manually.
ENV LC_ALL=en_US.UTF-8

RUN addgroup --gid 1000 coder; \
  adduser --uid 1000 --ingroup coder --home /home/coder --shell /bin/bash --disabled-password --gecos "" coder; \
  # Give the coder user sudo access
  usermod -a -G sudo coder; \
	echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Run as root user, before 'USER coder'
RUN USER=coder; \
  GROUP=coder; \
  # Get the fixuid package
  curl -SsL https://github.com/boxboat/fixuid/releases/download/v0.4/fixuid-0.4-linux-amd64.tar.gz | tar -C /usr/local/bin -xzf - && \
  # Make it available globally
  chown root:root /usr/local/bin/fixuid; \
  chmod 4755 /usr/local/bin/fixuid; \
  # Set fixuid configurations
  mkdir -p /etc/fixuid; \
  printf "user: $USER\ngroup: $GROUP\npaths:\n  - /home/coder\n  - /home/coder/project" > /etc/fixuid/config.yml

# Run as coder user from now on
USER coder

# Install the code-server executable
RUN cd /home/coder; \
  # Get the latest version number
  CODER_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/cdr/code-server/releases/latest)); \
  # Get the latest package based on version number
  wget --quiet https://github.com/cdr/code-server/releases/download/$CODER_VERSION/code-server$CODER_VERSION-linux-x64.tar.gz; \
  # Decompress it
  tar -xvzf code-server$CODER_VERSION-linux-x64.tar.gz; \
  # Make sure it is executable
  chmod +x /home/coder/code-server$CODER_VERSION-linux-x64/code-server; \
  # Make it globally callable
  sudo cp -r /home/coder/code-server$CODER_VERSION-linux-x64/code-server /usr/local/bin; \
  # This solves 'Error: ENOENT: no such file or directory, open '/src/packages/server/build/web/favicon.ico'
  sudo mkdir -p /src/packages/server/build/web; \
  sudo touch /src/packages/server/build/web/favicon.ico; \
  # Cleanup
  rm -rf /home/coder/code-server$CODER_VERSION-linux-x64 /home/coder/code-server$CODER_VERSION-linux-x64.tar.gz

EXPOSE 8443

# Install extensions and default settings
RUN \
  # Backups, extensions, etc., directories that VSCode uses
  mkdir -p /home/coder/.local/share/code-server/Backups; \
  mkdir -p /home/coder/.local/share/code-server/extensions; \
  mkdir -p /home/coder/.local/share/code-server/User; \
  #=====
  #===== Default settings =====
  # Set default font to 16px since 12px is way to small
  echo '{' > /home/coder/.local/share/code-server/User/settings.json; \
  #--- REMEMBER: use '>>' from now on, only the first one above uses '>' ---
  echo '  "editor.fontSize": 16,' >> /home/coder/.local/share/code-server/User/settings.json; \
  # Terminal font size
  echo '  "terminal.integrated.fontSize": 16,' >> /home/coder/.local/share/code-server/User/settings.json; \
  # Set default tab size to 2
  echo '  "editor.tabSize": 2,' >> /home/coder/.local/share/code-server/User/settings.json; \
  # Enable file autoSave after 1 second of inactivity
  echo '  "files.autoSave": "afterDelay",' >> /home/coder/.local/share/code-server/User/settings.json; \
  # Enable PHP syntax highlighting for some common Drupal php files
  echo '  "files.associations": {' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '    "*.inc": "php",' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '    "*.install": "php",' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '    "*.module": "php",' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '    "*.theme": "php"' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '  },' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '  "editor.fontFamily": "Monaco, 'Courier New', monospace",' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '  "git.autofetch": true, ' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '  "editor.wordWrap": on ' >> /home/coder/.local/share/code-server/User/settings.json; \
  echo '}' >> /home/coder/.local/share/code-server/User/settings.json; \
  #=====
  #===== Extensions =====
  ###
  ### Install GitLens extension
  # Make sure we're in the 'extensions' dir
  cd /home/coder/.local/share/code-server/extensions; \
  # Get the latest version
  GITLENS_V=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/eamodio/vscode-gitlens/releases/latest)); \
  # Remove the leading 'v'
  GITLENS_VER_NAME=$(echo $GITLENS_V | sed -e 's/^v//g'); \
  # Get the archive based on latest version
  wget --quiet https://github.com/eamodio/vscode-gitlens/releases/download/$GITLENS_V/gitlens-$GITLENS_VER_NAME.vsix; \
  # Unzip the archive
  mv gitlens-$GITLENS_VER_NAME.vsix gitlens-$GITLENS_VER_NAME.zip; \
  unzip -q gitlens-$GITLENS_VER_NAME.zip -d gitlens; \
  # Set the right dir name
  mv gitlens/extension eamodio.gitlens-$GITLENS_VER_NAME; \
  # cleanup
  rm -rf gitlens*

# We create first instead of just using WORKDIR as when WORKDIR creates, the user is root.
RUN mkdir -p /home/coder/project/code-server; chmod -R 765 /home/coder/project
WORKDIR /home/coder/project

# This assures we have a volume mounted even if the user forgot to do bind mount.
# XXX: Workaround for GH-459 and for OpenShift compatibility.
VOLUME [ "/home/coder/project" ]

ENTRYPOINT ["dumb-init", "fixuid", "code-server"]
