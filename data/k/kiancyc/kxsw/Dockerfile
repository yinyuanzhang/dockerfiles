# FROM buildkite/puppeteer

# WORKDIR /usr/src/app

# COPY . .

# RUN npm install

# EXPOSE 3000

# CMD [ "npm", "start" ]


FROM  alekzonder/puppeteer

WORKDIR /app

COPY . .

RUN yarn install

EXPOSE 3000

CMD [ "npm", "start" ]