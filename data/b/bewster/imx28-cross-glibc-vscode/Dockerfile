FROM bewster/debian-vscode-bc4:4.2.5_1.24.1_jessie

LABEL com.gbelectronics.vendor="GB Electronics (UK) Ltd" \
      com.gbelectronics.version="0.2-DEV"

# Switch to the rout user to be able to install packages
USER root

RUN dpkg --add-architecture i386                       \
 && apt-get update                                     \
 && apt-get install -y                                 \
		build-essential                                \
		libncurses5-dev                                \
		libncursesw5-dev                               \
		libc6-dev:i386                                 \
		zlib1g-dev:i386                                \
		lib32stdc++6                                   \
		git                                            \
		wget                                           \
 && apt-get clean                                      \
 && rm -rf /var/lib/apt/lists/*

# Install cross compiler
#ADD imx28-cross-glibc.tar.bz2 /opt
RUN wget ftp://ftp.embeddedarm.com/ts-arm-sbc/ts-7600-linux/cross-toolchains/imx28-cross-glibc.tar.bz2 -P /tmp/
RUN tar -C /opt -xvjf /tmp/imx28-cross-glibc.tar.bz2 \
 && rm /tmp/imx28-cross-glibc.tar.bz2

# Switch back to the vscode user to allow app to run
USER vscode

# Install vscode extensions
RUN code --install-extension ms-vscode.cpptools               \
 && code --install-extension mkloubert.vscode-deploy-reloaded
