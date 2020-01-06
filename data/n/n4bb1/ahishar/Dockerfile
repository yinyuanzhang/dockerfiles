FROM node:latest as build
WORKDIR /project
COPY ./ /project/
RUN yarn --frozen-lockfile --no-progress
RUN yarn build -c production

FROM kyma/docker-nginx
LABEL maintainer="https://github.com/n4bb12/ahishar"
COPY --from=build /project/dist/ahishar /var/www
VOLUME /var/www
