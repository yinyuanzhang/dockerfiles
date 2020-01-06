# FROM node:8-alpine
# RUN mkdir /home/app
# WORKDIR /home/app
# COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
# RUN npm install --silent
# RUN npm install -g @angular/cli
# COPY . .
# EXPOSE 4200
# CMD ng serve --host 0.0.0.0 --disableHostCheck true

# Stage 1
FROM node:8-alpine as node

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --silent

COPY . .

RUN npm run build

# Stage 2
FROM nginx:alpine

COPY --from=node /usr/src/app/dist/mds /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80