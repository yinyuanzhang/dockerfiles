FROM node:buster as builder
WORKDIR /App
RUN apt update && apt install yarn -y 
COPY . /App
RUN yarn install && yarn build

FROM nginx:alpine
COPY --from=builder /App/dist/ /usr/share/nginx/html
ADD ./nginx.conf /etc/nginx/nginx.conf
