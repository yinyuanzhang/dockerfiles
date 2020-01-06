FROM node
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN yarn
RUN yarn build

FROM nginx
COPY --from=0 /usr/src/app/.vuepress/dist /usr/share/nginx/html