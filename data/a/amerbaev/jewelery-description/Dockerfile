FROM node:lts-alpine as build
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install 
COPY . .
RUN npm run build

FROM nginx:stable-alpine as production
COPY --from=build app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
