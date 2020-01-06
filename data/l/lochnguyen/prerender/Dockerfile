FROM node:12

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update -y \
  && apt-get install google-chrome-stable -y \
  && apt-get clean \
  && rm -rf /tmp/* /var/lib/apt/lists/*

RUN groupadd -r prerender && useradd -r -g prerender -G audio,video prerender \
    && mkdir -p /home/prerender && chown -R prerender:prerender /home/prerender

WORKDIR /home/prerender
COPY . /home/prerender
RUN  npm install && chown -R prerender:prerender /home/prerender/


EXPOSE 3000
USER prerender
CMD ["node", "server.js"]