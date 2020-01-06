FROM nodered/node-red-docker

# Switch back to root user to install packages and configure entrypoint
USER root
RUN apt-get update && apt-get install -y \
    xvfb \
    x11-xkb-utils \
    xfonts-100dpi \
    xfonts-75dpi \
    xfonts-scalable \
    xfonts-cyrillic \
    x11-apps \
    clang \
    libdbus-1-dev \
    libgtk2.0-dev \
    libnotify-dev \
    libgnome-keyring-dev \
    libgconf2-dev \
    libasound2-dev \
    libcap-dev \
    libcups2-dev \
    libxtst-dev \
    libxss1 \
    libnss3-dev \
    gcc-multilib \
    g++-multilib \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY files/entrypoint /
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]

RUN mkdir -m 1777 /tmp/.X11-unix

# Switch back to node-red user to install the nbrowser module and run as non-root user
USER node-red
RUN npm install node-red-contrib-nbrowser

ENV DEBUG=nightmare
CMD ["npm", "start", "--", "--userDir", "/data"]
