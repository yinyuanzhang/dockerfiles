FROM node:10-slim

# See https://crbug.com/795759
RUN apt-get update && apt-get install -yq libgconf-2-4

# Install latest chrome dev package and fonts to support major charsets (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
# Note: this installs the necessary libs to make the bundled version of Chromium that Puppeteer
# installs, work.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# It's a good idea to use dumb-init to help prevent zombie chrome processes.
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

# Uncomment to skip the chromium download when installing puppeteer. If you do,
# you'll need to launch puppeteer with:
#     browser.launch({executablePath: 'google-chrome-unstable'})
#ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

# Add pptr user.
RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
    && mkdir -p /home/pptruser/Downloads \
    && chown -R pptruser:pptruser /home/pptruser 

RUN mkdir -p /tmp/gofetch/app && chown pptruser:pptruser /tmp/gofetch

# copy all files from repo to the app dir on the machine and give user access
ADD app /home/pptruser/gofetch/app
ADD public /home/pptruser/gofetch/public
COPY public /home/pptruser/gofetch/
COPY package.json /home/pptruser/gofetch/
COPY package-lock.json /home/pptruser/gofetch/
COPY tsconfig.json /home/pptruser/gofetch/
COPY yarn.lock /home/pptruser/gofetch/

RUN chown -R pptruser:pptruser /home/pptruser/gofetch/ && chown pptruser:pptruser /home/pptruser/gofetch/app/**/*.*

# Run user as non privileged.
USER pptruser

WORKDIR /home/pptruser/gofetch/

# install npm packages and transpile typescript files
RUN npm install
RUN npm run build

# Run everything after as non-privileged user.
EXPOSE 3031

ENTRYPOINT ["dumb-init", "--"]
CMD ["node","dist/src/index.js"]