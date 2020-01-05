FROM jenkins/slave:latest
USER root
RUN apt-get update && apt-get install -y software-properties-common && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g selenium-side-runner && npm install -g chromedriver --unsafe-perm=true --allow-root
RUN apt-get install -y libappindicator3-1 libatk-bridge2.0-0 libatspi2.0-0 libgtk-3-0 fonts-liberation libasound2 libgconf-2-4 libnspr4 libxss1 libnss3 xdg-utils wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb
#USER jenkins
