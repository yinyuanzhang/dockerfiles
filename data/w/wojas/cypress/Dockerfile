FROM cypress/base:8
ARG CYPRESS_VERSION=3.1.1
RUN npm install cypress@$CYPRESS_VERSION
RUN /node_modules/.bin/cypress verify
RUN mkdir /tests
WORKDIR /tests
ENTRYPOINT ["/node_modules/.bin/cypress"]
