FROM node:6.11.1

RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && apt-get update || true \
    && apt-get --yes install google-chrome-stable \
    && curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o chromedriver_linux64.zip \
    && cp chromedriver_linux64.zip /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver


