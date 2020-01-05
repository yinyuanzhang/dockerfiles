FROM node:10.15.3

WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .

CMD ["npm", "start"]
CMD ["npm", "run test", "run e2e"]