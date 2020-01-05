FROM node:10.14

RUN apt-get update && \
  apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi \
  xfonts-scalable xfonts-cyrillic x11-apps clang libdbus-1-dev libgtk2.0-dev \
  libnotify-dev libgnome-keyring-dev libgconf2-dev libasound2-dev libcap-dev \
  libcups2-dev libxtst-dev libxss1 libnss3-dev gcc-multilib g++-multilib

# Fixes "cannot run in wd" issue with some Lerna versions https://github.com/theia-ide/theia/issues/508
RUN npm config set unsafe-perm true

# Needed for yoman run in Docker
RUN mkdir -p /root/.config/configstore && chmod g+rwx /root /root/.config /root/.config/configstore