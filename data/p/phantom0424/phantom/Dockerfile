FROM node:8.11.1

# RUN npm config set registry https://registry.npm.taobao.org --global
# RUN npm config set disturl https://npm.taobao.org/dist --global
# RUN npm config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/ --global

WORKDIR /usr/src/app

COPY package.json .

RUN npm i --silent

COPY . .

RUN npm run build

EXPOSE 12001

CMD npm run start:prod
