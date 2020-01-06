# build
FROM node:9.11.1-alpine as build-stage
WORKDIR /app
COPY package*.json ./
COPY certs ./
RUN npm install
COPY . .
EXPOSE 443
RUN npm run build

ENTRYPOINT ["npm", "start"]

# deploy
#FROM nginx:1.13.12-alpine as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]