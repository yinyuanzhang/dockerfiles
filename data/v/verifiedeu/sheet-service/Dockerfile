FROM mhart/alpine-node:10

WORKDIR /app
COPY . .

RUN npm install

EXPOSE 80
CMD ["node", "./src/app.js"]
