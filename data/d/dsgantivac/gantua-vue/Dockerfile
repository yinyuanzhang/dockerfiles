# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH
COPY . /app
# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
RUN npm install express express-graphql graphql --save
RUN npm install --save axios
RUN npm install cors --save
RUN npm install downloadjs
RUN npm install --save firebase

EXPOSE 8050
# start app
CMD ["npm", "run", "serve"]
