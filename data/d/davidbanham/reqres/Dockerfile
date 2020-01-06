FROM node:7

WORKDIR /opt/app

COPY ./package.json /opt/app/package.json
RUN npm install

COPY . /opt/app/

EXPOSE 3000

ENV PORT=3000
CMD ["node", "app.js"]
