FROM node

EXPOSE 3000
COPY /src /var/discordbot

RUN cd /var/discordbot && npm install

CMD [ "node", "/var/discordbot/web" ]