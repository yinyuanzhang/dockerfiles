FROM node:8.4.0
RUN apt-get update -y
RUN apt-get install -y libgtk-3-0 libx11-xcb1 libnss3 libxss1 libgconf-2-4 libasound2 vim git
RUN node -v
RUN npm -v
RUN yarn -v

RUN git clone https://github.com/GoogleChrome/puppeteer
RUN cd puppeteer && git checkout -b v0.10.1 && yarn
RUN ln -s /puppeteer/.local-chromium/linux-497674/chrome-linux/chrome /usr/local/bin
RUN chrome --version
WORKDIR /home
