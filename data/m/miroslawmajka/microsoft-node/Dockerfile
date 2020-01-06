FROM mcr.microsoft.com/dotnet/core/sdk:2.1

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash --debug
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update -y

RUN apt-get -y update
RUN apt-get -yq install google-chrome-stable nodejs unzip

RUN wget https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver
