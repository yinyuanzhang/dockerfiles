FROM kocuoneu/test:core

WORKDIR /var/www
RUN mkdir app
COPY . /var/www/app
RUN npm --prefix ./app install

EXPOSE 8081
ENTRYPOINT ["node", "./app/index.js"]
