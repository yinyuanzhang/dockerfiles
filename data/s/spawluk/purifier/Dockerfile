FROM arm32v7/node

COPY qemu-arm-static /usr/bin

WORKDIR /home/node/app

COPY src/package*.json ./

RUN npm install

COPY src/ .

VOLUME [ "/home/node/app/config" ]

USER node

CMD [ "npm", "start" ]