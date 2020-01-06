# Dockerfile for running docker-compose and building / testing epiphany-ui in CircleCI 2.0
FROM circleci/node:8-stretch
USER root

RUN apt-get update \
    && apt-get install -y curl ssh git tar awscli unzip groff

# Install make sure the latest stable versions of npm and bower are installed globally
  # Uninstall and reinstall npm. Version that shipped with image is too old, and updating gave us a "Cannot find module 'strip-ansi'" error when running any npm command (ie npm-v), implying a hosed upgrade
RUN npm uninstall npm -g && curl -L https://www.npmjs.com/install.sh | sh
RUN npm install -g bower \
  # Run the NPM doctor for good measure
  && echo "\n*** Health Checks ***" \
  && echo "Running NPM doctor: \n$(npm doctor)\n" \
  # Make sure all our pieces are working correctly by running basic commands with them (aws, docker-compose, etc)
  && aws help > /dev/null \
  && echo "AWS CLI Version ...... = $(aws --version)\n" \
  && echo "Docker-Compose Version = \n$(docker-compose version)\n" \
  && echo "Node Version ......... = $(node -v)\n" \
  && echo "NPM Version .......... = $(npm -v)\n"