FROM node as dev

RUN npm install yarn 

ADD . /app

WORKDIR /app

RUN yarn install

RUN yarn build

CMD ["yarn", "start"]

FROM nginx

COPY --from=dev /app/build /app

COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf