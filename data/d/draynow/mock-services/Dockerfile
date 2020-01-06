FROM draynow/node-base

EXPOSE 9000

WORKDIR /app

COPY index.js /app/index.js
COPY mocks /app/mocks
COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock

RUN yarn install --production
CMD ["yarn", "start"]
