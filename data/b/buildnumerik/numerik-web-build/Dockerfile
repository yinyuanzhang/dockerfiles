FROM node:10
LABEL author="Simon <simon@simonrichards.me>"
RUN apt-get update && apt-get install -y lftp xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 chromium
RUN npm install cypress
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
# docker build . -t buildnumerik/numerik-web-build && docker push buildnumerik/numerik-web-build
