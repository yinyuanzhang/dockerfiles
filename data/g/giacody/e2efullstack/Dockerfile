FROM python:3.6.8-stretch

RUN apt update && apt install curl wget gnupg2 -y

# install chrome

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable xvfb

RUN apt-get update && apt-get install -f -y
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt install nodejs -y
RUN apt install libgdal-dev git -y

