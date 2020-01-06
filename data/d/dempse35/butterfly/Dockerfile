FROM node:10.12.0

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
# For npm@5 or later, copy package-lock.json as well
# COPY package.json package-lock.json 

RUN npm install -g

# Bundle app source
COPY . .

EXPOSE 3000

CMD [ "npm", "run", "server:prod" ]