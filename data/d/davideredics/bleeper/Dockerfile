FROM node:latest
WORKDIR /usr/src/app
COPY ["Bleeper/package.json", "Bleeper/package-lock.json*", "./"]
RUN npm ci
COPY Bleeper .
EXPOSE 8443
ENV NODE_ENV development
CMD npm start
