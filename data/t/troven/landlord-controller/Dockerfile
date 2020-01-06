FROM node:alpine

LABEL app="landlord-controller"
LABEL author="cto@troven.co"

RUN apk update && apk upgrade && apk add --no-cache bash git openssh

ENV NODE_ENV "production"

# Install the app

WORKDIR /opt/landlord/

COPY package.json package.json
COPY tsconfig.json tsconfig.json

# Add our source files

COPY config config
COPY src src

# Compile the code

RUN npm i -g typescript
RUN npm install
RUN npm run build

# Launch Landlord Controller

CMD ["npm", "run", "boot"]

