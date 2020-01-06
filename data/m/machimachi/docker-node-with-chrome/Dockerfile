FROM node:12.7.0

MAINTAINER machimachi <zxcvbnmtacashi@gmail.com>

# npm packages
RUN npm install yarn -g && chmod +x /usr/local/lib/node_modules/yarn/bin/yarn.js && yarn global add npm renovate

# chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo deb http://dl.google.com/linux/chrome/deb/ stable main > /etc/apt/sources.list.d/google.list && apt-get update && apt-get install -y dbus-x11 google-chrome-stable
    
