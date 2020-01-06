# base image
FROM node:8 as build-deps
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json package-lock.json ./
RUN npm install react-scripts@1.1.1 -g
#RUN yarn --ignore-engines
RUN npm install
COPY . ./
#RUN yarn build --ignore-engines
EXPOSE 8000
# start app
CMD ["npm", "start"]