FROM node:8.11.1

# install dependencies

WORKDIR /opt/app
# ENV "RUN_DIR=/opt/app"

COPY package.json package-lock.json* ./
RUN npm cache clean --force && npm install --verbose

# copy app source to image _after_ npm install so that
# application code changes don't bust the docker cache of npm install step
COPY . /opt/app


# set application PORT and expose docker PORT, 80 is what Elastic Beanstalk expects
# ENV PORT 3011
EXPOSE 3011
RUN npm install pm2 -g

#CMD [ "npm", "run", "start" ]
CMD ["pm2-runtime", "ecosystem.config.js", "--env", "development"]