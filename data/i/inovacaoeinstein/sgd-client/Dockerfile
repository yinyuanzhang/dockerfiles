FROM node

ENV NPM_CONFIG_LOGLEVEL warn

RUN mkdir -p /sgd
WORKDIR /sgd
COPY --chown=node:node ./ ./

RUN npm install
RUN chown node:node node_modules

CMD npm run start
	
EXPOSE 3000
