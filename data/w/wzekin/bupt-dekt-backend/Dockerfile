FROM node:buster as builder
WORKDIR /App
RUN apt update && apt install yarn -y && yarn global add @angular/cli && ng config -g cli.packageManager yarn
COPY . /App
RUN yarn install && ng build --prod --base-href './'

FROM nginx:alpine
COPY --from=builder /App/dist/bupt-dekt-backend /usr/share/nginx/html
ADD ./nginx.conf /etc/nginx/nginx.conf
