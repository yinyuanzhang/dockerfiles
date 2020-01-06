FROM node:10

# Add Chrome sources and PGP keys
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee -a /etc/apt/sources.list && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Install latest Chrome stable, Xvfb packages
RUN apt-get -q update -y && apt-get -q install -y  \
        google-chrome-stable \
        xvfb \
        gtk2-engines-pixbuf \
        xfonts-cyrillic \
        xfonts-100dpi \
        xfonts-75dpi \
        xfonts-base \
        xfonts-scalable \
        imagemagick \
        x11-apps \
        default-jre

# Run xvfb
RUN Xvfb :0 -ac -screen 0 1024x768x24 &

# Export display for Chrome
ENV DISPLAY :99

# Install karma
RUN npm install -g karma-cli

WORKDIR /app

CMD [ "karma", "start", "--single-run" ]