FROM bewster/debian-vscode:1.24.1_jessie

LABEL com.gbelectronics.vendor="GB Electronics (UK) Ltd" \
      com.gbelectronics.version="0.1-DEV"

# Switch to the rout user to be able to install packages
USER root

RUN dpkg --add-architecture i386                       \
 && apt-get update                                     \
 && apt-get install -y                                 \
        libqtgui4                                      \
        libqtwebkit4                                   \
        poppler-utils                                  \
        wget                                           \
        gdebi-core                                     \
 && apt-get clean                                      \
 && rm -rf /var/lib/apt/lists/*

# Install Beyond Compare
RUN wget https://www.scootersoftware.com/bcompare-4.2.5.23088_amd64.deb -P /tmp/
RUN gdebi --non-interactive /tmp/bcompare-4.2.5.23088_amd64.deb \
 && rm /tmp/bcompare-4.2.5.23088_amd64.deb

# Switch back to the vscode user to allow app to run
USER vscode
