FROM node:10 as build

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev vim

ENV NODE_ROOT /usr/app/
RUN mkdir -p $NODE_ROOT
WORKDIR $NODE_ROOT
COPY . .

RUN npm install -g @angular/cli
RUN yarn install
# RUN npm rebuild node-sass --force

RUN ng build --prod --output-path=dist

############
### prod ###
############

FROM nginx:alpine

# copy artifact build from the 'build environment'
COPY --from=build /usr/app/dist /usr/share/nginx/html

COPY nginx/docker.nginx.conf /etc/nginx/conf.d/default.conf.dis
COPY nginx/run.sh /run.sh

EXPOSE 80

CMD ["sh", "/run.sh"]
