FROM node:10.14.2
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production
COPY . .
EXPOSE 8080
CMD node server/index.js