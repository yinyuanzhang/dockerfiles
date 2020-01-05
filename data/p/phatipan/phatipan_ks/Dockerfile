FROM node:10.15.3-alpine

# next
ENV NODE_ENV production

ENV TEST_FILE=test.js

WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --production --silent && mv node_modules ../

COPY . .

RUN node ${TEST_FILE}
EXPOSE 8080
CMD npm start