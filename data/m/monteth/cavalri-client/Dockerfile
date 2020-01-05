# build stage
FROM node:12.13-stretch as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

#FROM nginx:1
#
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY dist /usr/share/nginx/html
#
#EXPOSE 80
#RUN chown nginx.nginx /usr/share/nginx/html/ -R