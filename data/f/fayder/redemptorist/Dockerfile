FROM node:carbon

RUN git clone https://jrfay08:4f6c37fc7eee09b48644d0235d61c29cbf827657@github.com/JackFay/redemptorist /app/

RUN git config --global user.email "jrfay08@gmail.com" && git config --global user.name "Redemptorist Website"

WORKDIR /app

RUN npm install && cd ./client && npm install && cd ..

RUN cp /app/client/webpack.config.prod.js /app/client/node_modules/react-scripts/config

RUN cd ./client && npm run build && cd ./build/static/js && rm *.map && cd /app && npm run build-prod

env PORT=8080

env NODE_ENV=production

EXPOSE 8080

CMD ["node", "dist"]
