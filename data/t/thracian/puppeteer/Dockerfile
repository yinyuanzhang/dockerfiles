FROM node:10-slim

ENV SONAR_SCANNER_VERSION "3.3.0.1492-linux"
ENV PATH="/home/pptruser/bin:${PATH}"

# Install latest chrome dev package and fonts to support major charsets (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
# Note: this installs the necessary libs to make the bundled version of Chromium that Puppeteer
# installs, work.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update \
  && apt-get install -y git openssh-client locales google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont unzip \
  xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 \
  procps \
  --no-install-recommends \ 
  && wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  && unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} \  
  && cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner sonar-scanner && chmod +x sonar-scanner \   
  && rm -rf /var/lib/apt/lists/* \
  && rm -f https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip

# If running Docker >= 1.13.0 use docker run's --init arg to reap zombie processes, otherwise
# uncomment the following lines to have `dumb-init` as PID 1
# ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
# RUN chmod +x /usr/local/bin/dumb-init
# ENTRYPOINT ["dumb-init", "--"]

# Uncomment to skip the chromium download when installing puppeteer. If you do,
# you'll need to launch puppeteer with:
#     browser.launch({executablePath: 'google-chrome-unstable'})
# ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

# Install puppeteer so it's available in the container.
RUN npm i puppeteer \
  # Add user so we don't need --no-sandbox.
  # same layer as npm install to keep re-chowned files from using up several hundred MBs more space
  && groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
  && mkdir -p /home/pptruser/Downloads \
  && chown -R pptruser:pptruser /home/pptruser \
  && chown -R pptruser:pptruser node_modules \
  && chown -R pptruser:pptruser sonar-scanner-${SONAR_SCANNER_VERSION}

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8     

RUN runuser -l pptruser -c 'curl https://pre-commit.com/install-local.py | python3 -'
# Run everything after as non-privileged user.
USER pptruser

CMD ["google-chrome-unstable"]
