FROM node:12.10.0-alpine as react-build
WORKDIR /app
COPY . ./
RUN npm rebuild node-sass
RUN yarn config set network-timeout 600000 -g
RUN yarn install
RUN yarn run build
FROM nginx:alpine
COPY /nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=react-build /app/build /usr/share/nginx/html
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]