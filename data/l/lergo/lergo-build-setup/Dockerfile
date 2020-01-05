FROM ubuntu:16.04

RUN apt update -y
RUN apt install -y wget

# https://askubuntu.com/questions/510056/how-to-install-google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update -y
RUN apt-get install google-chrome-stable -y

RUN apt install git -y

RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
RUN . ~/.nvm/nvm.sh && nvm install `wget -O - https://raw.githubusercontent.com/lergo/lergo-ri/develop/.nvmrc` > /dev/null
RUN . ~/.nvm/nvm.sh && nvm alias default

## used for phantomjs - which will be deprecated soon
RUN apt install bzip2 -y
RUN apt update -y && apt upgrade -y && apt install python3-pip -y
RUN pip3 install awscli --upgrade
RUN apt install mongodb -y
RUN apt install nginx -y
