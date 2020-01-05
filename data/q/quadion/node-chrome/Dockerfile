FROM node:10.18-jessie-slim
RUN apt-get update
RUN apt-get install chromium xvfb --yes

# See https://crbug.com/795759
RUN apt-get install -yq libgconf-2-4

# Install latest chrome dev package and fonts to support major charsets (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
# Note: this installs the necessary libs to make the bundled version of Chromium that Puppeteer
# installs, work.
RUN apt-get install -y wget --no-install-recommends \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qqy \
    && apt-get install -qqy ${CHROME_VERSION:-google-chrome-stable} fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont --no-install-recommends \
    && apt-get purge --auto-remove -y curl \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/* /src/*.deb