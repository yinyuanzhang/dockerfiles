FROM node:10.15

# Originally from Dan Lynn <docker@danlynn.org>

RUN npm set progress=false
RUN npm install -g ember-cli@3.6.0

# install google-chrome
RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
ENTRYPOINT ["/usr/src/app/node_modules/ember-cli/bin/ember"]
CMD ["help"]
