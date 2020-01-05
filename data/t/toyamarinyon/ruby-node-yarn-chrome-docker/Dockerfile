FROM ruby:2.5

# Install dependencies
RUN apt-get update -qq && apt-get install -y apt-transport-https build-essential libpq-dev libappindicator1 \
    fonts-liberation libasound2 libgconf-2-4 libgtk-3-0 libnspr4 libnss3 libx11-xcb1 libxss1 libxtst6 lsb-release \
    xdg-utils unzip

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update -qq && apt-get install -y yarn

# Install node
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && apt-get install nodejs

# Install chrome
RUN  curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
     dpkg -i google-chrome-stable_current_amd64.deb

# Install chrome-driver
RUN curl -O https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/
