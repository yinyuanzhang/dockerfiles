FROM nodesource/trusty:0.10

WORKDIR /tmp/app

RUN apt-get update
RUN apt-get install -y phantomjs
RUN npm install -g karma karma-cli karma-jasmine karma-phantomjs-launcher
RUN apt-get clean

ENTRYPOINT ["/usr/bin/karma"]