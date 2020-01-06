FROM debian:stable-slim

RUN apt-get update
RUN apt-get install -yy wget curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
	apt-get update && apt-get install -y nodejs && \
  npm i -g npm@6
RUN apt-get install -y git

RUN node -v && npm -v

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable xvfb
RUN npm -v
RUN apt update && apt install -y procps
RUN apt clean
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan git.anixe.pl >> ~/.ssh/known_hosts
