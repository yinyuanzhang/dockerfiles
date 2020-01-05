FROM cypress/base:10.16.0
MAINTAINER  Luke Barnes

ENV APP_HOME=/usr/app
WORKDIR $APP_HOME

RUN npm install cypress@3.1.5

ENV CYPRESS_DIR=$APP_HOME/node_modules/.bin

RUN echo $CYPRESS_DIR
RUN export PATH="$PATH:$CYPRESS_DIR"

# Updates path variable to include cypress 
ENV PATH "$PATH:$CYPRESS_DIR"

RUN cypress verify
