# stage 1
FROM node:10.14.2 as node
WORKDIR /app
COPY . .
RUN npm install
RUN npm audit fix
RUN npm install -g @angular/cli@8.0.1
RUN ng build --prod --output-hashing=all

# stage 2
FROM nginx:1.13
COPY --from=node /app/dist/group-offerta /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
