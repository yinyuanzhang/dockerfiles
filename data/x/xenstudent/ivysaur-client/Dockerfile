FROM node:alpine as builder
WORKDIR '/app'
COPY ./package.json ./
RUN npm install
RUN npm install -g @angular/cli
COPY . .
RUN ng build --prod

FROM nginx
EXPOSE 4200
# ENV NGINX_HOST=foobar.com
# ENV NGINX_PORT=8080
# COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html