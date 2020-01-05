# CWRC-GitServer

FROM node

WORKDIR /apps/CWRC-GitServer

COPY . .

RUN npm install
RUN npm install pm2 -g

EXPOSE 3000
CMD ["pm2", "start", "./bin/www", "--no-daemon"]
