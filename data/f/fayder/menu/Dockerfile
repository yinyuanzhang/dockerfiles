FROM node:carbon

RUN git clone https://jrfay08:4f6c37fc7eee09b48644d0235d61c29cbf827657@github.com/JackFay/Menu /app/


WORKDIR /app

RUN npm install && npm install serve -g

RUN mv /app/webpack.config.dev.js /app/node_modules/react-scripts/config

RUN mv /app/webpack.config.prod.js /app/node_modules/react-scripts/config

RUN apt-get update && apt-get -y install nano && apt-get -y install lsof

RUN npm run build && cd ./build/static/js && rm *.map && cd /app && cd /app/Server && npm install && npm run build

EXPOSE 3000

CMD ["npm", "run", "prod"]

# CMD ["serve", "-s", "build", "-l", "3000"]