FROM node:carbon

RUN git clone https://jrfay08:4f6c37fc7eee09b48644d0235d61c29cbf827657@github.com/JackFay/menuBackend /app/

RUN apt-get update && apt-get install lsof && apt-get install nano

WORKDIR /app

RUN npm install && npm run build

EXPOSE 18080

CMD ["node", "dist"]