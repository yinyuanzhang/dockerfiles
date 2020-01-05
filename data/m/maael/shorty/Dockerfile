FROM mhart/alpine-node:11
WORKDIR /repo
COPY . .

ENV NODE_ENV=production

RUN yarn
RUN yarn build
RUN yarn install --production --ignore-scripts --prefer-offline

EXPOSE 3000

CMD ["node", "server/index.js"]
