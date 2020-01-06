FROM node:boron

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json .
# For npm@5 or later, copy package-lock.json as well
# COPY package.json package-lock.json .

RUN npm install
RUN npm install forever -g

# Bundle app source
COPY . .

EXPOSE 4000
CMD [ "forever", "app.js" ]
