FROM node:6.9

VOLUME /var/games/minecraft
#arbitrarily assigned ports for 5 servers. change if you need to.
EXPOSE 8443 25565-25569

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#i want jdk8, so enable debian testing
RUN echo "deb http://ftp.us.debian.org/debian/ testing main" >> /etc/apt/sources.list

#update and accept all prompts
RUN apt-get update -y && apt-get install -y \
  rdiff-backup \
  screen \
  openjdk-8-jre-headless \
  git \
  rsync \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/hexparrot/mineos-node.git /usr/src/app
RUN cd /usr/src/app
RUN npm install --production && npm install bcrypt
RUN cp /usr/src/app/mineos.conf /etc/mineos.conf
COPY auth.js /usr/src/app

#generate a cert. sync before generating to avoid an error
RUN chmod +x generate-sslcert.sh; \
  sync; \
  ./generate-sslcert.sh

RUN useradd mc; \
  echo "mc:admin" | chpasswd

CMD [ "npm", "start" ]
