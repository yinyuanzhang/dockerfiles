FROM node:8.7.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN ["chmod", "+x", "/usr/src/app/wait-for-it.sh"]

EXPOSE 3000

CMD ["npm", "run start"]
