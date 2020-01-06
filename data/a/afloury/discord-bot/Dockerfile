
FROM node:latest

RUN mkdir /app
WORKDIR /app

RUN git init
RUN git remote add origin https://github.com/afloury/discord-bot.git
RUN git fetch origin
RUN git reset --hard FETCH_HEAD

RUN mkdir -p /app/{commands,node_modules}
RUN npm install discord.js
RUN npm install discord.js-commando --save

# OLD WAY

#COPY index.js  /app/
#COPY commands/* /app/commands/
#COPY node_modules/* /app/node_modules/
#COPY package.json /app/
#WORKDIR /app/

ENTRYPOINT node /app/index.js
