FROM node:9

# Install Chrome

RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        xvfb \
		lftp \
		zip \
		unzip \
        google-chrome-stable \
        sudo

ADD scripts/xvfb-chrome /usr/bin/xvfb-chrome
RUN ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome

ENV CHROME_BIN /usr/bin/google-chrome

RUN npm i npm@latest -g

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

RUN sudo npm install --unsafe-perm node-sass -g

RUN node -v
RUN npm -v
# RUN apt-cache policy chromium | grep Installed | sed -e "s/Installed/Chrome/"
