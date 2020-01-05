FROM node:10
# create working directory
RUN mkdir -p /usr/src/app
# set working directory
WORKDIR /usr/src/app
COPY . .

RUN yarn install --frozen-lockfile && yarn build

CMD ["node", "./server.js"]
