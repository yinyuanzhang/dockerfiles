FROM node:carbon

RUN git clone https://jrfay08:4f6c37fc7eee09b48644d0235d61c29cbf827657@github.com/JackFay/traderBackend -b simulator /app/

WORKDIR /app

RUN npm install && cd ./client && npm install && cd ..

RUN mv /app/client/webpack.config.prod.js /app/client/node_modules/react-scripts/config && cd /app/client && npm run build && cd /app

env PORT=8080

EXPOSE 8080

CMD ["npm", "run", "simulator"]
