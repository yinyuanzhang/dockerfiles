FROM node:10
COPY ./ /app
WORKDIR /app
ENV CI 1
RUN npm install && npm run buildbeta

FROM nginx:1
RUN mkdir /app
COPY --from=0 /app/dist-beta /app
COPY nginx.conf /etc/nginx/nginx.conf
