# this file is based on
# https://github.com/ebidel/try-puppeteer/blob/a956034/backend/Dockerfile
# and
# https://github.com/GoogleChrome/puppeteer/blob/395c506/docs/troubleshooting.md#running-puppeteer-in-docker

FROM node:8-slim

# See https://crbug.com/795759
RUN apt-get update && apt-get install -yq libgconf-2-4

# Install latest chrome dev package and fonts to support major charsets
# (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
# Note: this installs the necessary libs to make the bundled version of
# Chromium that Puppeteer installs, work.
RUN apt-get update && apt-get install -y wget --no-install-recommends \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \
      --no-install-recommends \
    && apt-get install -y procps \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge --auto-remove -y curl \
    && rm -rf /src/*.deb

# chrome uses many processes, to see this run

# $ ps aux| grep -i chrome | wc -l

# because of chrome’s process hunger, issues may arise where “zombie” processes
# appear as a result of termination signals not being handled properly by the
# root process at PID 1 which in this case is our little proxy server. look at
# the ticket https://github.com/GoogleChrome/puppeteer/issues/1825 to see why
# this can be problematic. to address this, there is a minimal signal manager
# (or “process supervisor”), called dumb-init, which can be used to make the
# behaviour of the process at PID 1 more typical of a “proper” linux system. we
# install it here and set it as our ENTRYPOINT to allow it to sit at PID 1 and
# manage signals in a more typical manner, which includes reaping zombies.
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

# Add pptr user.
RUN groupadd -r pptr && useradd -r -g pptr -G audio,video pptr \
    && mkdir -p /home/pptr/Downloads \
    && chown -R pptr:pptr /home/pptr

# copy our files in
COPY package.json           /app/package.json
COPY chrome-headless.sh     /app/chrome-headless.sh
COPY proxy.js               /app/proxy.js

# set up permissions
RUN chmod u+x /app/chrome-headless.sh
RUN chown -R pptr:pptr /app

# switch to chrome user for npm install
USER pptr
WORKDIR /app
RUN npm install

# override entrypoint from base image
EXPOSE 3000
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "proxy.js"]
