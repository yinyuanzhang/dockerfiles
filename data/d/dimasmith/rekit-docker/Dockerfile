FROM node:carbon

# Dev servier port
EXPOSE 6075

# Studio port
EXPOSE 6076

# Build port
EXPOSE 6077

# Update npm and yarn
RUN npm install npm@latest -g 
RUN npm install yarn -g 
RUN yarn global add rekit

VOLUME /home/node/app
WORKDIR /home/node/app

CMD ["yarn", "start"]