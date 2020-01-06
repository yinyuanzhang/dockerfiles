FROM keymetrics/pm2:latest-alpine

ADD . /www.bianjie.ai
WORKDIR /www.bianjie.ai
RUN npm i && npm run build
EXPOSE 3000
ENV NODE_ENV="production"
CMD ["pm2-runtime", "server.js"]
