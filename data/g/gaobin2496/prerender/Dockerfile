FROM debian:stretch

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -qqy \
  && apt-get -qqy install \
       git gnupg wget ca-certificates apt-transport-https xz-utils \
       ttf-wqy-zenhei --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable --no-install-recommends \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN useradd headless --shell /bin/bash --create-home \
  && usermod -a -G sudo headless \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'headless:nopassword' | chpasswd

RUN mkdir /data && chown -R headless:headless /data

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 8.9.4
ENV ARCH=x64

RUN wget -O "node-v$NODE_VERSION-linux-$ARCH.tar.xz" "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz"  \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN  cd /data \
&& git clone https://github.com/prerender/prerender.git \
&& cd prerender \
&& npm install

USER headless

WORKDIR /data/prerender

EXPOSE 3000

CMD [ "npm", "start" ]
