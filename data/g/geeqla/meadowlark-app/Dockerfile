FROM node:10
ENV NODE_ENV=production
WORKDIR /usr/src/meadowlark-app
COPY . .
RUN yarn global add pm2
RUN yarn install
EXPOSE 3000
CMD yarn start