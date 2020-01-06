FROM ubuntu:latest as base

MAINTAINER Kunai

RUN apt-get update

# Install java
RUN apt-get install --yes --fix-missing openjdk-8-jre

# Install Python
RUN apt-get install --yes python3
RUN apt-get install --yes python3-pip

# Install pytest
RUN pip3 install pytest

# Install git
RUN apt-get install --yes git-core

# Install Node, NPM, Yarn
RUN apt-get install --yes curl
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install --yes nodejs npm yarn

# Install Chrome
#RUN apt-get update
#RUN apt-get purge chromium-browser
#RUN apt-get install --yes lsb-release
#RUN apt-get install --yes wget
#RUN apt-get install --yes fonts-liberation
#RUN apt-get install --yes libappindicator3-1
#RUN apt-get install --yes libxss1
#RUN apt-get install --yes xdg-utils
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN dpkg -i google-chrome-stable_current_amd64.deb
## chromedriver also needs to be installed.
#RUN wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
#RUN apt-get install --yes zip
#RUN unzip chromedriver_linux64.zip
#RUN mv chromedriver /usr/bin/chromedriver
#RUN chown root:root /usr/bin/chromedriver  # questionable - may need to add other user permissions
#RUN chmod a+x /usr/bin/chromedriver

# Install Chromium
RUN apt-get update
RUN apt-get install --yes chromium-browser

# Install some tools...
RUN apt-get install --yes wget
RUN apt-get install --yes zip

# Install PhantomJS
RUN wget 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2'
RUN tar xvjf phantomjs-1.9.8-linux-x86_64.tar.bz2
RUN mv phantomjs-1.9.8-linux-x86_64 /usr/local/share
RUN ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin


# Install Sonar Scanner
RUN mkdir /opt/sonarscanner
WORKDIR /opt/sonarscanner
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip
RUN unzip *.zip
RUN rm *.zip
RUN ln -s /opt/sonarscanner/sonar-scanner-*/bin/sonar-scanner /bin/sonar-scanner

