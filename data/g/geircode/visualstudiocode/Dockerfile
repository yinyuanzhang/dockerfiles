FROM ubuntu

RUN apt-get update \
 && apt-get install -y curl apt-transport-https libgtk2.0-0 libxss1 libasound2 xauth x11-apps dbus git gpg dbus-x11 libx11-xcb1 python3 python3-pip sudo

RUN mkdir /var/run/dbus

RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
 && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
 && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

RUN apt-get update \
 && apt-get install -y code \
 && apt-get install -f

RUN cp /usr/lib/x86_64-linux-gnu/libxcb.so.1 /usr/share/code/ \
 && cp /usr/lib/x86_64-linux-gnu/libxcb.so.1.1.0 /usr/share/code/ \
 && sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/share/code/libxcb.so.1 \
 && sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/share/code/libxcb.so.1.1.0

ENV DISPLAY=10.0.75.1:0.0
ENV USER=dev
ENV GROUP=developers

# RUN groupadd $GROUP
# RUN useradd -m -G $GROUP,sudo $USER

# The session needs to run on a non-root user in order to connect to the x11 server. 
# Use "sudo -s" and password "dev" to become root in the Container for development purposes
RUN useradd -m $USER && echo "$USER:$USER" | chpasswd && adduser $USER sudo

USER $USER

WORKDIR /home/$USER

ENTRYPOINT /usr/bin/code --verbose