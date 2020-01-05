FROM node:10.13-alpine
ENV NODE_ENV production
WORKDIR C:\Dev\Node\Dareto\NodeProject
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install
COPY . .
EXPOSE 8080
CMD npm start