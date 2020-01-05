FROM mhart/alpine-node
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "yarn.lock",  "npm-shrinkwrap.json*", "./"]
RUN yarn install --production --silent && mv node_modules ../
RUN npm i -g pm2
COPY . .
EXPOSE 3001
CMD yarn run docker 
