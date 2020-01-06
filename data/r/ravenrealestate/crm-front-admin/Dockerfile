FROM node:10.17

# Create app directory
RUN mkdir -p /usr/src/app/proj_front
WORKDIR /usr/src/app/proj_front

# Install app dependencies
COPY package.json /usr/src/app/proj_front/package.json

RUN yarn install

EXPOSE 3000
EXPOSE 3001

CMD [ "yarn", "run", "start" ]
