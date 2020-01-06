FROM node:carbon

RUN git clone https://jrfay08:4f6c37fc7eee09b48644d0235d61c29cbf827657@github.com/JackFay/Inked /app/

WORKDIR /app

RUN npm install

RUN mv /app/webpack.config.prod.js /app/node_modules/react-scripts/config

RUN cd ./Server && npm install && cd .. && npm install -g serve

RUN npm run build

env PORT=3000

EXPOSE 3000

CMD ["npm", "run", "prod"]
