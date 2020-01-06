FROM node:8.10

EXPOSE 3001
ENV APP_ROOT=/usr/src/app

# Install dumb-init to rape any Chrome zombies
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb
RUN dpkg -i dumb-init_*.deb

# Install Chromium.
RUN \
  wget --no-check-certificate -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
RUN google-chrome-stable --no-sandbox --version > /opt/chromeVersion

# Add prerender user.
RUN mkdir -p ${APP_ROOT}
RUN chgrp -R 0 ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT}

WORKDIR ${APP_ROOT}

COPY package-lock.json ${APP_ROOT}
COPY package.json ${APP_ROOT}
RUN npm install
COPY . ${APP_ROOT}
RUN npm run build

CMD [ "dumb-init", "npm", "start" ]
