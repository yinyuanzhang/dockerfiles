FROM circleci/node:6-browsers

WORKDIR /home/circleci/app

#prepare to install
RUN sudo apt-get update

# install a bunch of binaries for usage by build scripts
# first AWS stuff
RUN sudo apt-get install -y --no-install-recommends python-dev python-pip libgconf-2-4
RUN sudo pip install awscli && sudo pip install awsebcli

# # update some permissions
RUN sudo chmod -R go+rw ${HOME}
RUN sudo chmod -R go+rw /home/circleci/app
RUN sudo chown -R circleci /home/circleci/app
RUN sudo chgrp -R circleci /home/circleci/app
#RUN sudo chown -R circleci ~/.npm
#RUN sudo chgrp -R circleci ~/.npm
RUN sudo chown -R circleci $(npm config get prefix)/lib/node_modules
RUN sudo chown -R circleci $(npm config get prefix)/bin
RUN sudo chown -R circleci $(npm config get prefix)/share

# make sure git knows who we are
RUN git config --global user.email "botty@mcbotface.com" && \
    git config --global user.name "Botty McBotface" && \
    git config --global core.filemode false

# update chrome
RUN curl --silent --show-error --location --fail --retry 3 --output /tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
      && (sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb || sudo apt-get -fy install)  \
      && rm -rf /tmp/google-chrome-stable_current_amd64.deb \
      && sudo sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-sandbox|g' \
           "/opt/google/chrome/google-chrome" \
      && google-chrome --version

RUN export CHROMEDRIVER_RELEASE=$(curl --location --fail --retry 3 http://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
      && curl --silent --show-error --location --fail --retry 3 --output /tmp/chromedriver_linux64.zip "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_RELEASE/chromedriver_linux64.zip" \
      && cd /tmp \
      && unzip chromedriver_linux64.zip \
      && rm -rf chromedriver_linux64.zip \
      && sudo mv chromedriver /usr/local/bin/chromedriver \
      && sudo chmod +x /usr/local/bin/chromedriver \
      && chromedriver --version

# install npm
# thanks https://stackoverflow.com/questions/44269086/how-to-upgrade-npm-to-npm5-on-the-latest-node-docker-image
RUN yarn global add npm@5.4.0
