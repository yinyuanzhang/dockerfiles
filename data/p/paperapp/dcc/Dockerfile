FROM node:8.11.2
# deprecated https://docs.docker.com/engine/reference/builder/#maintainer-deprecated TODO fix if needed or remove?
MAINTAINER "Shane Fast" <shane@get-paper.com>
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list \
&& apt-get update \
&& apt-get install -y -qq curl \

&& apt-get clean
# RUN yum clean all
RUN curl -o /usr/local/bin/jq http://stedolan.github.io/jq/download/linux64/jq \
&& chmod +x /usr/local/bin/jq
RUN apt-get -y install wget
# INSTALL pip and aws cli
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools \
        groff \
        less \
    && pip3 install --upgrade pip \
    && apt-get clean

RUN pip3 --no-cache-dir install --upgrade awscli

RUN npm i -g npm
RUN npm install gulp mocha eslint snyk apidoc license-checker npm-cli-login npm-check-updates -g
RUN npm install angular angular-mocks babel-core babel-preset-es2015 bower chai chai-http eslint gulp gulp-concat gulp-eslint gulp-htmlmin gulp-minify-ejs gulp-json-modify gulp-mocha gulp-ng-annotate gulp-uglify gulp-uglifycss mocha mock-aws-s3 node-mocks-http request run-sequence sinon supertest yargs
# Define working directory.
WORKDIR /data
CMD ["-"]
ENTRYPOINT ["jq"]
