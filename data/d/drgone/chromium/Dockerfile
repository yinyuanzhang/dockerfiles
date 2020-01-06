FROM buildpack-deps:jessie

RUN groupadd --gid 1000 chromium \
  && useradd --uid 1000 --gid chromium --shell /bin/bash --create-home chromium

RUN apt-get update && apt-get install -y --force-yes libxcomposite-dev libx11-xcb-dev libxcursor-dev libxdamage-dev libxi-dev libxtst-dev libnss3-dev libcups2-dev libxss-dev libxrandr-dev libgconf-2-4 libasound2-dev libatk1.0-dev libgtk-3-dev
RUN apt-get install -y --force-yes libfreetype6 libfontconfig unzip

ENV CHROMIUM_VERSION 548153

RUN cd / && wget -mS https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/${CHROMIUM_VERSION}/chrome-linux.zip && unzip storage.googleapis.com/chromium-browser-snapshots/Linux_x64/${CHROMIUM_VERSION}/chrome-linux.zip && ln -s /chrome-linux/chrome /usr/bin/chromium

