from node:10.6

RUN apt-get update
RUN apt-get -y install git p7zip

COPY . .

RUN npm init -y
RUN npm install
RUN npm run build

CMD ["npm", "run", "package"]
