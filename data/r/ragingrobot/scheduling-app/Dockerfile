FROM node:11
RUN mkdir /scheduling-app
ADD . /scheduling-app
WORKDIR /scheduling-app
RUN npm i
EXPOSE 8080 3000
CMD ["npm", "start"]