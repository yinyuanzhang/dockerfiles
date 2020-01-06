FROM node:10.15.2 as builder
WORKDIR  /app
COPY . .
RUN npm install -g create-react-app &&\
    npm install
RUN npm run build

FROM nginx
COPY --from=builder /app/build/ /usr/share/nginx/html/
RUN chown -R nginx:nginx /usr/share/nginx/html/
COPY ./nginx.conf /etc/nginx/nginx.conf