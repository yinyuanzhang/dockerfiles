FROM node:8.8.1

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . $HOME/.nvm/nvm.sh && nvm install v8.2.1 && nvm use v8.2.1

RUN apt-get update && apt-get install -y python3-dev python3 python3-pip zip
RUN curl -O https://bootstrap.pypa.io/get-pip.py
#RUN python get-pip.py
RUN pip3 install awscli
RUN pip3 install requests
RUN npm install -g gulp
RUN npm install -g gulp-cli

RUN curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip
RUN unzip sonar-scanner-cli-3.2.0.1227-linux.zip
RUN chmod +x sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner


