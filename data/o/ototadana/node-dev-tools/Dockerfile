FROM node:0.11.14
MAINTAINER ototadana@gmail.com

RUN npm install -g bower grunt-cli yo

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable openjdk-7-jdk sudo unzip vim xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/node -m -s /bin/bash node
RUN mkdir -p /app && chown node:node /app
RUN echo "node ALL=(ALL) NOPASSWD:ALL" >>/etc/sudoers


ENV DISPLAY :99

COPY ./config/. /config/
RUN chmod -R +x /config/*

USER node
VOLUME ["/tools", "/app"]
WORKDIR /app

ENTRYPOINT ["/config/entrypoint"]
