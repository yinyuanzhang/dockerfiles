FROM node:carbon
ENV NODE_ENV=production
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN npm install -g @vue/cli
RUN npm install
#RUN npm run build
CMD ['./node_modules/.bin/vue-cli-service', 'build']