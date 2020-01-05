FROM bewster/debian-vnc-desktop:jessie

LABEL com.gbelectronics.vendor="GB Electronics (UK) Ltd" \
      com.gbelectronics.version="0.2-DEV"

# Additional OS packages required
RUN apt-get update                                     \
 && apt-get install -y                                 \
        curl                                           \
        apt-transport-https                            \
        libxss1                                        \
 		    git                                            \
 && apt-get clean                                      \
 && rm -rf /var/lib/apt/lists/*

# Install Visual Studio Code
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
 && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg                                  \
 && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list' \
 && apt-get update                                                                         \
 && apt-get install -y                                                                     \
        code                                                                               \
 && apt-get install -f                                                                     \
 && apt-get clean                                                                          \
 && rm -rf /var/lib/apt/lists/*

# Copy the startup script and run it
#ADD vscode-startup.sh /
#RUN chmod +x /vscode-startup.sh

# Copy new bits from root to tmp
RUN cp /root/.vnc/xstartup /tmp                                                   \
 && cp /root/.xscreensaver /tmp

ENV \
  USER=vscode

# Create a user to run vscode
RUN useradd -ms /bin/bash vscode
USER vscode
WORKDIR /home/vscode

# Copy new bits to vscode
RUN mkdir ~/.vnc                                                                    \
 && cp /tmp/xstartup ~/.vnc                                                         \
 && cp /tmp/.xscreensaver .

# Workaround to get vscode to run under VNC
RUN mkdir ~/lib                                                                     \
 && cp /usr/lib/x86_64-linux-gnu/libxcb.so.1 ~/lib                                  \
 && sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' ~/lib/libxcb.so.1                         \
 && echo -n "alias vscode='LD_LIBRARY_PATH=$HOME/lib code'"'\n' >> ~/.bash_aliases

# Launch the command and run
#CMD ["/bin/bash", "/vscode-startup.sh", "--no-exit"]
