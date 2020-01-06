FROM webratio/ant:1.10.1

# Installs NodeJS and GIT
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN sudo apt-get install -y nodejs && \
    apt-get install -y git
RUN npm install sfdx-cli --global
RUN sfdx plugins:install salesforcedx@45.3.4
