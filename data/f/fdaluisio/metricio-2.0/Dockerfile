FROM node:8

ENV PATH /usr/src/app/node_modules/.bin:$PATH
ENV NODE_ENV=production
ENV PORT=3000
ENV BABEL_DISABLE_CACHE=1

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --only=production

COPY . .

#RUN npm install webpack webpack-cli -g

RUN webpack -p

RUN chgrp -R 0 /usr/src/app && \
    chmod -R g=u /usr/src/app

USER 1000
#RUN mv dist /dist

EXPOSE 3000

CMD npm start
