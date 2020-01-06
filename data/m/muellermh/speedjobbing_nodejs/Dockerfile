FROM node:boron
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN npm install -g gulp --allow-root
RUN npm install -g bower --allow-root
COPY package.json /usr/src/app/
RUN npm install --allow-root
COPY bower.json /usr/src/app/
RUN bower install --allow-root
COPY . /usr/src/app
EXPOSE 3000

CMD [ "gulp" ]