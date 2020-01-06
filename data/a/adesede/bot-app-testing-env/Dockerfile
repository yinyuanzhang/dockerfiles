FROM node:12-alpine
ENV NODE_ENV production
ADD ["entrypoint.sh", "package-lock.json", "package.json", "/app/"]
WORKDIR /app
RUN mkdir screen
RUN npm install
ADD ["src/index.js", "src/config.js", "src/helper.js", "/app/src/"]
ENTRYPOINT ["/app/entrypoint.sh"]
