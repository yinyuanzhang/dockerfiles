FROM node:10.16.0
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install && npm cache clean --force && npm install sails -g
#RUN ["apt-get", "update"]
#RUN ["apt-get", "install", "-y", "vim"]
ENV TZ=Europe/Brussels
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . .
EXPOSE 3001
ENV PORT 3001
# - then it needs to start container with command 'tini -- node ./bin/www'
# CMD ["forever", "start" ,"./app.js","--prod"]
# CMD ["node","./app.js","--prod"]
CMD ["node","./app.js"]