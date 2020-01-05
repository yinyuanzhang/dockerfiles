# stage 1
FROM node:latest as node
WORKDIR /app
COPY . .
RUN npm config set unsafe-perm true

RUN npm install
RUN npm rebuild node-sass
RUN npm install -g http-server


# # stage 2
# FROM nginx:alpine
# COPY --from=node /app/dist/receptenv2 /usr/share/nginx/html
EXPOSE 8080

RUN npm run build

CMD [ "npm", "start" ]



# FROM node:8-alpine

# # Create app directory
# WORKDIR /usr/src/appdock

# COPY . .

# RUN npm config set unsafe-perm true

# RUN npm i -g yarn

# # Install app dependencies
# RUN yarn

# EXPOSE 3000

# RUN yarn build

# CMD [ "yarn", "start" ]
# view rawDockerfile hosted with ❤ by GitHub