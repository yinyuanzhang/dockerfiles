FROM node:13.0.1

WORKDIR /app

COPY package.json ./package.json
COPY package-lock.json ./package-lock.json

RUN npm install --production --no-audit

COPY index.js ./index.js

EXPOSE 7000

CMD [ "/bin/sh", "-c", "node ./index.js" ]

