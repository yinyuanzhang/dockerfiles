FROM circleci/node:8

RUN sudo apt-get update && sudo apt-get install -y apt-transport-https && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN sudo apt-get update && sudo apt-get install -y yarn && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*

RUN sudo rm /usr/local/bin/yarn
