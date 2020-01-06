FROM node:8

LABEL description="Validates the schema of OpenAPI 3.0 API definition files"
WORKDIR /home/node

COPY oas3validator oas3validator
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN ln -s /home/node/oas3validator /usr/local/bin/oas3validator

USER node
RUN npm i

ENTRYPOINT ["oas3validator"]
