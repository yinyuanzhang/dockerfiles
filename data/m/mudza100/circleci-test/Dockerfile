FROM node:carbon

# Create app directory
WORKDIR /circleci-test

COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

EXPOSE 8000
CMD npm "start"
