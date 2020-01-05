FROM node:10.15.3
COPY . /gateway
WORKDIR /gateway
RUN npm i
RUN npx rimraf .env
CMD ["npm", "run", "start"]