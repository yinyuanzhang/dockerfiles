FROM node:10-alpine

WORKDIR /opt/pogmeter
COPY package.json /opt/pogmeter/package.json
RUN npm install
COPY . /opt/pogmeter
RUN cd static && npm install && npm run build
EXPOSE 4000

CMD ["npm", "start"]