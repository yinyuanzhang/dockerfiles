FROM node:8

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
  apt-get update -y && \
  apt-get install -y google-chrome-stable && \
  groupadd -r prerender && \
  useradd -r -g prerender -G audio,video prerender && \
  mkdir -p /home/prerender/prerender && \
  chown -R prerender:prerender /home/prerender && \
  wget https://github.com/fuww/prerender/archive/master.tar.gz -O - | \
  tar --strip-components 1 -xzC /home/prerender/prerender && \
  rm -rf /var/lib/apt/lists/*

USER prerender
WORKDIR /home/prerender/prerender

ENV NODE_ENV=production
RUN npm install

EXPOSE 3000
CMD node server.js
