FROM circleci/clojure:lein-2.7.1

RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
RUN heroku plugins:install heroku-cli-deploy
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN sudo npm install -g webpack mocha

#Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN sudo apt-get update
RUN sudo apt-get install -y xvfb google-chrome-unstable
