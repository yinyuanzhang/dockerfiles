FROM node
LABEL application="todobackend"

COPY . /app
WORKDIR /app

RUN npm install -g mocha && \
npm install

ENTRYPOINT ["mocha"]