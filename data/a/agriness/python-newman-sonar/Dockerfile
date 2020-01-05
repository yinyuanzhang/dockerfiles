FROM zbyte64/docker-python-node

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . $HOME/.nvm/nvm.sh && nvm install v8.2.1 && nvm use v8.2.1

RUN apt-get install -y zip
RUN apt-get update && apt-get install -y python3-dev  build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
RUN curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip
RUN unzip sonar-scanner-cli-3.2.0.1227-linux.zip
RUN npm install newman --global