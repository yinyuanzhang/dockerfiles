FROM killercentury/nodejs-bower-grunt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY package.json /usr/src/app/
ONBUILD RUN npm install
ONBUILD COPY bower.json .bowerrc* /usr/src/app/
ONBUILD RUN bower install --allow-root
ONBUILD COPY . /usr/src/app
ONBUILD RUN [ -f "Gruntfile.js" ] && grunt build || /bin/true
ONBUILD ENV NODE_ENV production

CMD [ "npm", "start" ]