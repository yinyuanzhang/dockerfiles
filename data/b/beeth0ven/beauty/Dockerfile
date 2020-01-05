FROM node:10.16.3

WORKDIR /server
COPY . /server

RUN npm install
RUN npm run build

CMD ["npm", "run", "release"]
