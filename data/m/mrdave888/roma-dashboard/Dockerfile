FROM node:8.14.0-jessie
RUN curl https://install.meteor.com/ | sh
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . ./
RUN meteor npm install
RUN meteor build --directory /usr/src/app --allow-superuser
RUN cd /usr/src/app/bundle/programs/server && npm install
CMD ["node", "./bundle/main.js"]
